#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Read APT code from a text file and extract feedrate and coordinates (x, y, z) from lines
beginning with GOTO. Generates a text file with values:
    (feedrate, x, y, z)
where feedrate can be RAPID or a number.
"""

import math
import io

def apt2toolpath(apt_code):
    """
    Returns a list with the coordinates (feedrate, x, y, z) of the GOTO instructions    
    """
    result = []
    point0 = []
    feedrate = 'RAPID'                                  # By default
    buf = io.StringIO(apt_code)
    for line in buf:
        line = ' '.join(line.split())                   # Collapse multiple spaces into one

        if line=='RAPID':
            feedrate = 'RAPID'
#                print('feedrate = %s' % feedrate)

        word1 = line.split(' ')[0].split('/')[0]        # First word without '/'

        if word1=='FEDRAT':
            str_fedrat, str_args = line.split("/")      # Separate FEDRAT and feedrate value
            str_number, str_units = str_args.split(",") # Separate feedrate number and units
            feedrate = round(float(str_number), 5)
#                print('feedrate = %s' % feedrate)
            
        if word1=='GOTO':
            str_goto, str_coords = line.split("/")      # Separate GOTO and coordinates
            str_x, str_y, str_z = str_coords.split(",") # Get coordinates
            x = round(float(str_x), 5)                  # String to float with 5 decimals
            y = round(float(str_y), 5)
            z = round(float(str_z), 5)
#                print('   (%s, %s, %s)' % (x, y, z))
            point1 = [x, y, z]
            if point1 == point0:
                print("Warning: duplicated point (%f, %f, %f) removed" % (x, y, z))
            else:
                point0 = [x, y, z]
                result.append([feedrate, x, y, z])
                
    return result


if __name__ == '__main__':
    f = open('example.aptsource', 'r')
    apt = f.read()
    f.close()
    
    toolpath = apt2toolpath(apt)
    
    f = open('example.toolpath', 'w')
    for i in toolpath:
#        print(i)
        f.write('%s %s %s %s\n' % (i[0], i[1], i[2], i[3]))
    f.close()

