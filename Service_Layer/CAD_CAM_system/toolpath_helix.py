#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Domingo Morales Palma <dmpalma@us.es>

"""

from math import pi, sin, cos
import csv          # CSV File Reading and Writing
import numpy as np
import matplotlib.pyplot as plt

def toolpath_helix(instance_name, R, h, df=95.8, f=1000, sd=0.2):
    '''
    Generate a helical path for the tooltip.
    Save cartesian coordinates (x, y, z) to a CSV file.

    Function arguments:
    instance_name: defines the CSV file path
    R:      Tool radius [mm]
    h:      final flange height
    df:     Final diameter of the hole-flanged sheet [mm] (default 95.8)
    f:      Tool feedrate [mm/min] (default 1000)
    sd:     Tool step-down [mm/rev] (default 0.2)

    Internal variables:
    t:      Time [s]
    a, r:   Angular [degrees] and radial [mm] coordinates (polar axes)
    x, y:   In-plane coordinates [mm] (cartesian axes)
    z:      Vertical coordinate [mm] (decreasing value, z<0)
    v:      Tool feedrate [mm/s]
    w:      Angular speed w = v/r [degrees/s]
    '''
    # File name
    filename = 'toolpath.csv'
    filepath = 'Data_Layer/%s/%s' % (instance_name, filename)

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
    v = f/60                # Tool feedrate [mm/s]
    w = v/r * 180/pi        # Angular speed [degrees/s]
    dt = da/w               # Increment of time [s]

    f0 = open(filepath, 'w')
    f0.write('%.3f, %.3f, %.3f\n' % (x, y, z))

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
        # Coordinates of the tool path
        f0.write('%.3f, %.3f, %.3f\n' % (x, y, z))
        i += 1


    f0.close()
    
    plot_toolpath(filepath)

    return filename


def plot_toolpath(toolpath_file):
    image_format = 'png'
    image_dpi = 90
#    plt.rcParams["figure.figsize"] = (7.48, 6)
#    plt.rcParams["font.family"] = 'sans-serif'
#    plt.rcParams["font.sans-serif"] = 'Arial, Helvetica, sans-serif'
#    plt.rcParams["font.size"] = 8
#    plt.rcParams["lines.linewidth"] = 1
#    plt.rcParams["lines.markersize"] = 3

    print('Plotting 3D trajectory of the tool tip:')

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    #==============================================================================
    # theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    # z = np.linspace(-2, 2, 100)
    # r = z**2 + 1
    # x = r * np.sin(theta)
    # y = r * np.cos(theta)
    #==============================================================================

    x, y, z = [], [], []
    with open(toolpath_file, 'r') as csvfile:
        fieldnames = ['x', 'y', 'z']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            x.append(float(row['x']))
            y.append(float(row['y']))
            z.append(float(row['z']))

    ax.plot(x, y, z, label='Helical tool path')

    print('  Start tool path: (%.1f, %.1f, %.1f)' % (x[0], y[0], z[0]))
    print('  End tool path: (%.1f, %.1f, %.1f)' % (x[-1], y[-1], z[-1]))

    zmin = z[-1]
    ax.set_zlim([zmin, 0])
    ax.legend()
    plt.savefig(toolpath_file + '.' + image_format, dpi=image_dpi, format=image_format)
    plt.show()
    plt.close()
    


