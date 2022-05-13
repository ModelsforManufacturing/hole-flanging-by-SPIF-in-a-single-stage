#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Domingo Morales Palma <dmpalma@us.es>

Read toolpath data from data files and plot them in 3D figures.
It is useful to debug the toolpath generation code.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_toolpath(instance_name, toolpath_code):
    gcode = 'nc-program.gcode'
    toolpath_file = 'Data_Layer/%s/%s' % (instance_name, toolpath_code)
    gcode_file = 'Data_Layer/%s/%s' % (instance_name, gcode)

    image_format = 'png'
    image_dpi = 90
    plt.rcParams["figure.figsize"] = (7.48, 6)
    plt.rcParams["font.family"] = 'sans-serif'
    plt.rcParams["font.sans-serif"] = 'DejaVu Sans, Arial, Helvetica, sans-serif'
    plt.rcParams["font.size"] = 8
    plt.rcParams["lines.linewidth"] = 1
    plt.rcParams["lines.markersize"] = 3

    print('')
    print('Plotting 3D trajectory of the tool tip:')

    fig = plt.figure()
    #ax = fig.gca(projection='3d') --> Valid for matplotlib version prior to 1.0.0
    ax = Axes3D(fig)

    #==============================================================================
    # theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    # z = np.linspace(-2, 2, 100)
    # r = z**2 + 1
    # x = r * np.sin(theta)
    # y = r * np.cos(theta)
    #==============================================================================

    x, y, z = np.genfromtxt(toolpath_file, dtype='float')
    ax.plot(x, y, z, label='Helical tool path')

    x1 = x[-1]
    y1 = y[-1]
    z1 = z[-1]
    print('  (%.1f, %.1f, %.1f): end tool path' % (x1, y1, z1))

    zmin = z[-1]
    ax.set_zlim([zmin, 0])
    ax.legend()
    plt.savefig(gcode_file + '.' + image_format, dpi=image_dpi, format=image_format)
    
    return gcode


'''
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x1, y1, z1, 'b', linewidth=0.5, label='Stage 1')
ax.set_xlim([-50, 50])
ax.set_ylim([-50, 50])
ax.set_zlim([zmin, 0])
ax.legend()
ax.view_init(10., -60)
ax.set_xticks([]) 
ax.set_yticks([]) 
ax.set_zticks([])
plt.savefig('fig/toolpath_3d_1.' + image_format, dpi=image_dpi, format=image_format)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x1r, y1r, z1r, label='Retract')
ax.set_xlim([-50, 50])
ax.set_ylim([-50, 50])
ax.set_zlim([zmin, 0])
ax.legend()
plt.savefig('fig/toolpath_3d_1r.' + image_format, dpi=image_dpi, format=image_format)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x2a, y2a, z2a, label='Approach')
ax.set_xlim([-50, 50])
ax.set_ylim([-50, 50])
ax.set_zlim([zmin, 0])
ax.legend()
plt.savefig('fig/toolpath_3d_2a.' + image_format, dpi=image_dpi, format=image_format)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x2, y2, z2, 'b', linewidth=0.5, label='Stage 2')
ax.set_xlim([-50, 50])
ax.set_ylim([-50, 50])
ax.set_zlim([zmin, 0])
ax.legend()
ax.view_init(10., -60)
ax.set_xticks([]) 
ax.set_yticks([]) 
ax.set_zticks([])
plt.savefig('fig/toolpath_3d_2.' + image_format, dpi=image_dpi, format=image_format)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x1r, y1r, z1r, 'r--', linewidth=0.5, label='Retract')
ax.plot(x2a, y2a, z2a, 'b', linewidth=0.5, label='Approach')
ax.set_xlim([-50, 50])
ax.set_ylim([-50, 50])
ax.set_zlim([zmin, 0])
ax.legend(loc='upper right')
ax.view_init(10., -60)
ax.set_xticks([]) 
ax.set_yticks([]) 
ax.set_zticks([])
plt.savefig('fig/toolpath_3d_2ra.' + image_format, dpi=image_dpi, format=image_format)
'''


