#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def count_data(data, R):
    count = 0
    for i in range(len(data)):
        if type(data)==list:
            if data[i][0] == R:
                count += 1
        elif data.dtype.names:
            if data['R'][i] == R:
                count += 1
    return count

def get_data(data, R):
    x, y = [], []
    for i in range(len(data)):
        if type(data)==list:
            if data[i][0] == R:
                x.append(data[i][1])
                y.append(1 - data[i][2])
        elif data.dtype.names:
            if data['R'][i] == R:
                x.append(data['HER'][i])
                y.append(1 - data['t_t0'][i])
    return x, y

def get_transition(data, R):
    x, y = get_data(data, R)
    return x[1], y[1]

def get_lfr(data, R):
    x, y = get_data(data, R)
    i = x.index(max(x))
    return x[i], y[i]


def plot_her_t(data_SPIF, diagram_file):
    '''
    Format of data_SPIF: list of [R, HER, (t0-t)/t0]
    '''

    image_format = 'png'
    image_dpi = 100

#    plt.rcParams["figure.figsize"] = (5.51, 4)
#    plt.rcParams["font.family"] = 'sans-serif'
#    plt.rcParams["font.sans-serif"] = 'Arial, Helvetica, sans-serif'
#    plt.rcParams["font.size"] = 8
#    plt.rcParams["lines.linewidth"] = 1
#    plt.rcParams["lines.markersize"] = 3

    fig, ax = plt.subplots()

    Ri = 0.5
    t0 = 1.6
    df = 95.8
    #ramp = lambda her: ((her-1)/.05) if her < 1.05 else 1
    h_gap = (Ri+t0) - (Ri+t0/2)*np.pi/4 + Ri
    h_lim = lambda her: (1-1/her)/2 + h_gap/df #*ramp(her)
    #tr = lambda her: (1-1/her**2)/(4*h_lim(her))
    aa = t0/df/2
    cc = lambda her: -(1-1/her**2)/(4*(h_lim(her)-Ri/df))
    cc = lambda her: -(1-1/her**2)/(4*h_lim(her))
    tr = lambda her: (-1 + (1-4*aa*cc(her))**0.5)/(2*aa)
    her = np.arange(1.15, 1.81, 0.01)
    curve = [1-tr(x) for x in her]
    ax.plot(her, curve, '-', color='grey', linewidth=0.5)
    ax.text(1.68, 0.285, r'$\overline{\varepsilon_m} = 0$', rotation=5)


    # LFR: only for 2 or more values
    c6  = count_data(data_SPIF, 6)
    c8  = count_data(data_SPIF, 8)
    c10 = count_data(data_SPIF, 10)
    if c6 > 1:
        x1, y1 = get_lfr(data_SPIF, 6)
    if c8 > 1:
        x2, y2 = get_lfr(data_SPIF, 8)
    if c10 > 1:
        x3, y3 = get_lfr(data_SPIF, 10)
    if c6 > 1 and c8 > 1 and c10 > 1:
        lfr, = ax.plot([x1,x2,x3], [y1,y2,y3], 'k-', linewidth=2)
    elif c6 > 1 and c8 > 1:
        lfr, = ax.plot([x1,x2], [y1,y2], 'k-', linewidth=2)
    elif c6 > 1 and c10 > 1:
        lfr, = ax.plot([x1,x3], [y1,y3], 'k-', linewidth=2)
    elif c8 > 1 and c10 > 1:
        lfr, = ax.plot([x2,x3], [y2,y3], 'k-', linewidth=2)
    else:
        lfr = mlines.Line2D([], [], color='black')


    x, y = get_data(data_SPIF, 10)
    spif10, = ax.plot(x, y, 'b-', marker='o', markerfacecolor='white')
    x, y = get_data(data_SPIF, 8)
    spif8, = ax.plot(x, y, 'g-', marker='o', markerfacecolor='white')
    x, y = get_data(data_SPIF, 6)
    spif6, = ax.plot(x, y, 'r-', marker='o', markerfacecolor='white')

    ax.legend((spif10, spif8, spif6, lfr), ('R10', 'R8', 'R6', 'Forming limit'))


    ax.set_xlabel('Hole expansion ratio, $HER=d_f/d_0$')
    ax.set_ylabel('Non-dimensional thickness reduction, $1-\overline{t}/t_0$')
    ax.axis([1, 1.8, 0, 0.6])

    fig.tight_layout()
    plt.savefig(diagram_file, dpi=image_dpi, format=image_format)
    plt.show()
    plt.close()
    
    
if __name__ == '__main__':
    import os
    os.chdir('../..')
    data = np.genfromtxt('Data_Layer/files/data_SPIF.csv', names=True)
    data = np.array([
        [6, 1.16, 0.70], 
        [6, 1.35, 0.66], 
        [6, 1.45, 0.56], 
        [6, 1.46, 0.53], 
        [8, 1.16, 0.73], 
        [8, 1.46, 0.66], 
        [8, 1.51, 0.61], 
        [8, 1.55, 0.56], 
        [10, 1.16, 0.75],
        [10, 1.46, 0.71],  
        [10, 1.55, 0.66],  
        [10, 1.63, 0.58],  
        [10, 1.65, 0.56],  
        ])
    data = [
        [6, 1.16, 0.70], 
        [6, 1.35, 0.66], 
        [6, 1.45, 0.56], 
        [6, 1.46, 0.53], 
        [8, 1.16, 0.73], 
        [8, 1.46, 0.66], 
        [8, 1.51, 0.61], 
        [8, 1.55, 0.56], 
        [10, 1.16, 0.75],
        [10, 1.46, 0.71],  
        [10, 1.55, 0.66],  
        [10, 1.63, 0.58],  
        [10, 1.65, 0.56],  
        ]
    plot_her_t(data, 'Service_Layer/plot_results/diagram_HER_t.png')
