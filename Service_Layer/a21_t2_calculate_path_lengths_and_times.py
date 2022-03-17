#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Read toolpath code from a text file with (feedratem x, y, z) in lines, calculate distance and time between points and generate a text file with values:
    (time, x, y, z).
'''

import math
import io

RAPID = 12000                                       # mm/min, machining center EMCO VMC-200

def distance(point0, point1):
    ''' Distance between 2 points '''
    return math.sqrt((point0[0] - point1[0])**2 + (point0[1] - point1[1])**2 + (point0[2] - point1[2])**2)


def time(point0, point1, v):
    ''' Time [s] to travel between 2 points in a straight line [mm] at a speed v [mm/s] '''
    d = distance(point0, point1)
    return d/v

def toolpath2time(toolpath):
    ''' Read a list of lists (feedrate, x, y, z) and return another list of lists (time, x, y, z) '''

    first = toolpath.pop()
    result = [[0, first[1], first[2], first[3]]]    # first point at t=0
    
    point0 = [first[1], first[2], first[3]]
    t, dt = 0, 0
    for line in toolpath:
        f = line[0]
        x = line[1]
        y = line[2]
        z = line[3]

        if f == 'RAPID':
            f = RAPID                               # substitute RAPID by its value
        v = f/60                                    # mm/min to mm/s

        point1 = [x, y, z]
        
        dt = time(point0, point1, v)
        t1 = round(t + dt, 5)
        if t1 - t > 1e-5:                           # avoid repeat same time value
            t = t1
            result.append([t, x, y, z])
        
        point0 = point1

    return result


if __name__ == '__main__':
    f = open('example.toolpath', 'r')
    toolpath_file = f.read()
    f.close()

    toolpath = []
    buf = io.StringIO(toolpath_file)
    for line in buf:
        str_f, str_x, str_y, str_z = line.split(" ") # Get feedrate and coordinates
        if str_f == 'RAPID':
            f = 'RAPID'
        else:
            f = float(str_f)
        x = float(str_x)
        y = float(str_y)
        z = float(str_z)
        toolpath.append([f, x, y, z])
    
    time = toolpath2time(toolpath)
    
    f = open('example.time', 'w')
    for i in time:
#        print(i)
        f.write('%s %s %s %s\n' % (i[0], i[1], i[2], i[3]))
    f.close()

