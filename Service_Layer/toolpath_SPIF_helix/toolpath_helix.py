#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Generates a helical path for the tooltip.
The initial position (x, y, z) of the tooltip is saved to a text file.
From this initial position, time and local coordinates are saved to 3 text files:
    (t, X-X0), (t, Y-Y0), (t, Z-Z0).

Variables:
t: time
a, r: angular and radial axis (polar coordinates)
x, y: cartesian coordinates
z: vertical axis (decreasing value, z<0)
v: tool feedrate
w: angular feedrate, w = v/r
"""

from math import pi, sin, cos

def toolpath_helix(instance, R, h, df=95.8, f=1000, sd=0.2):
    # Name files
    filename = 'toolpath.csv'
    filepath = 'Data_Layer/%s/%s' % (instance, filename)
    data_tooltip_loc = 'Data_Layer/%s/toolpath-0.dat' % instance
    data_toolpath_X  = 'Data_Layer/%s/toolpath-X.dat' % instance
    data_toolpath_Y  = 'Data_Layer/%s/toolpath-Y.dat' % instance
    data_toolpath_Z  = 'Data_Layer/%s/toolpath-Z.dat' % instance
    data_intervals   = 'Data_Layer/%s/toolpath-intervals.dat' % instance

    # Global parameters
    R                       # Tool radius [mm]
    df                      # Final diameter of the hole-flanged sheet [mm]
    sd                      # Tool step-down [mm/rev]
    v = f/60                # Tool feedrate [mm/s]

    # Flange height
    h_max = { 6: 23.6, 
              8: 24.8, 
             10: 26.8}      # Set of values for {R: maximum flange height}
    if h == 0:
        h = h_max[R]        # Setting maximum flange height

    # Incremental position of tooltip
    da = 2                  # Increment of angle [degrees]
    N = 360/da              # Number of intervals per revolution
    dz = -sd/N              # Increment of z (<0) [mm]
    Nrev = int((h+R)/sd)    # Total number of revolutions
    Ni = N * Nrev           # Total number of iterations


    ### INITIAL POSITION

    # Global coordinates of the tooltip initial position:
    t = 0
    a = 0
    z = 0
    r = df/2 - R
    x = r
    y = 0
    w = v/r * 180/pi        # Angular speed [degrees/s]
    dt = da/w               # Increment of time [s]

#    print('Tooltip position at the beginning of the forming process:')
#    print('   (%.3f, %.3f, %.3f) mm  --> "%s"' % (x, y, z, data_tooltip_loc))
    f0 = open(filepath, 'w')
    f0.write('0, %.3f, %.3f, %.3f\n' % (x, y, z))

    ### ITERATIVE CALCULATION
    i = 1
    while i <= Ni:
        a += da
        a_rad = a * pi/180
        z += dz
        x = r * cos(a_rad)
        y = r * sin(a_rad)
        t += dt
    #    print('i=%d: a=%0.0fº: r=%.3f mm,, z=%.3f mm, x=%.3f mm, y=%.3f mm, t=%.3f s' % (i, a, r, z, x, y, t))
        # Time and coordinates of the tool path
        f0.write('%.3f, %.3f, %.3f, %.3f\n' % (t, x, y, z))
        i += 1


    f0.close()


#    print('Total iterations: %d --> "%s"' % (Ni, data_intervals))
#    print('Total time for simulation (mass scaling): %.3f s' % t)

    return filename
