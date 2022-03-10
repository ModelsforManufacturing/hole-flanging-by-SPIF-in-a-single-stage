#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Read toolpath code from a text file with (time, x, y, z) in lines and generate 4 text files with values:
    (x0, y0, z0), (time, x-x0), (time, y-y0) and (time, z-z0)
'''

import math
import io

def create_toolpath_files_for_abaqus(toolpath, directory=''):
    ''' Read a text string with lines (time, x, y, z) and create 4 files: (x0, y0, z0), (time, x-x0), (time, y-y0) and (time, z-z0) '''
    file_from = '%stoolpath-from.csv' % directory
    file_x = '%stoolpath-x.csv' % directory
    file_y = '%stoolpath-y.csv' % directory
    file_z = '%stoolpath-z.csv' % directory

    line1 = toolpath.pop()                          # Extract and remove first element
    t0, x0, y0, z0 = line1[0], line1[1], line1[2], line1[3]
#    print("First point (%s, %s, %s)" % (x0, y0, z0))

    f = open(file_from, 'w')
    f.write('%s %s %s' % (x0, y0, z0))              # save (x0, y0, z0) to file
    f.close()
    
    fx = open(file_x, 'w')
    fy = open(file_y, 'w')
    fz = open(file_z, 'w')

    fx.write('0.0 0.0\n')                           # Coordinates (0, 0, 0) in t=0
    fy.write('0.0 0.0\n')
    fz.write('0.0 0.0\n')

    for line in toolpath:
        t, x, y, z = line[0], line[1], line[2], line[3]

        fx.write('%s %s\n' % (t, x-x0))          # save (t, x-x0) to file
        fy.write('%s %s\n' % (t, y-y0))          # save (t, y-y0) to file
        fz.write('%s %s\n' % (t, z-z0))          # save (t, z-z0) to file

    fx.close()
    fy.close()
    fz.close()

    return (file_from, file_x, file_y, file_z)


if __name__ == '__main__':
    f = open('example.time', 'r')
    toolpath_file = f.read()
    f.close()
    
    toolpath = []
    buf = io.StringIO(toolpath_file)
    for line in buf:
        str_t, str_x, str_y, str_z = line.split(" ") # Get time and coordinates
        t = float(str_t)
        x = float(str_x)
        y = float(str_y)
        z = float(str_z)
        toolpath.append([t, x, y, z])
    
    filenames = create_toolpath_files_for_abaqus(toolpath)
    print (filenames)

