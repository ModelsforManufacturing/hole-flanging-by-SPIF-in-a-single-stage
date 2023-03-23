#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Domingo Morales Palma <dmpalma@us.es>

"""

import csv          # CSV File Reading and Writing
import textwrap     # Text wrapping and filling

gcode_head = textwrap.dedent('''\
    %2002
    G57
    T0300
    G00 X0.000 Y0.000 Z50.000
    G00 X0.000 Y0.000 Z21.000
    G01 X0.000 Y0.000 Z1.000 F1000
    ''')

gcode_tail = textwrap.dedent('''\
    G00 Z80.000
    G00 Y120.000
    M30
    ''')

def toolpath2gcode(instance_name, toolpath_code):
    gcode = 'nc-program.gcode'
    toolpath_file = 'Data_Layer/%s/%s' % (instance_name, toolpath_code)
    gcode_file = 'Data_Layer/%s/%s' % (instance_name, gcode)

    with open(gcode_file, 'w') as f1:
        head = gcode_head.splitlines()
        f1.write('%s\n' % head.pop(0))           # partno
        
        count = 1
        step = 2
        for line in head:
            f1.write('N%04d %s\n' % (count*step, line))
            count = count + 1

        with open(toolpath_file, 'r') as csvfile:
            fieldnames = ['x', 'y', 'z']
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            for row in reader:
                x, y, z = float(row['x']), float(row['y']), float(row['z'])
                g1 = 'N%04d G01 X%.3f Y%.3f Z%.3f\n' % (count*step, x, y, z)
                f1.write(g1)
                count = count + 1

        tail = gcode_tail.splitlines()
        for line in tail:
            f1.write('N%04d %s\n' % (count*step, line))
            count = count + 1

    return gcode
    
if __name__ == '__main__':
    import os
    os.chdir('../..')

    toolpath2gcode('R6-d635','toolpath.csv')
    
