import os
import sys
from py2gcode import gcode_cmd
from py2gcode import cnc_laser

dxfFileName = sys.argv[1]

layerList = ['vector{}'.format(i+1) for i in range(4)]

for layer in layerList:
    prog = gcode_cmd.GCodeProg()
    prog.add(gcode_cmd.GenericStart())
    prog.add(gcode_cmd.Space())
    
    param = {
            'fileName'    :  dxfFileName,
            'layers'      :  [layer,],
            'dxfTypes'    :  ['LINE','ARC'],
            'laserPower'  :  350,
            'feedRate'    :  60,
            'convertArcs' :  True,
            'startCond'   : 'minX',
            'direction'   : 'ccw',
            'ptEquivTol'  :  0.4e-3,
            }
    
    vectorCut = cnc_laser.VectorCut(param)
    prog.add(vectorCut)
    
    prog.add(gcode_cmd.Space())
    prog.add(gcode_cmd.End(),comment=True)
    
    baseName, ext = os.path.splitext(dxfFileName)
    ngcFileName = '{0}_{1}.ngc'.format(baseName,layer)
    prog.write(ngcFileName)


prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())


param = {
        'fileName'    :  dxfFileName,
        'layers'      :  layerList,
        'dxfTypes'    :  ['LINE','ARC'],
        'laserPower'  :  350,
        'feedRate'    :  60,
        'convertArcs' :  True,
        'startCond'   : 'minX',
        'direction'   : 'ccw',
        'ptEquivTol'  :  0.4e-3,
        }

vectorCut = cnc_laser.VectorCut(param)
prog.add(vectorCut)

prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)

baseName, ext = os.path.splitext(dxfFileName)
ngcFileName = '{0}.ngc'.format(baseName)
prog.write(ngcFileName)
