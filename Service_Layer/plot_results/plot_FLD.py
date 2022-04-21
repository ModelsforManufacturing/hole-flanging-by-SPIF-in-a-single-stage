#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (5.51, 4)
plt.rcParams["font.family"] = 'sans-serif'
plt.rcParams["font.sans-serif"] = 'Arial, Helvetica, sans-serif, DejaVu Sans'
plt.rcParams["font.size"] = 8
plt.rcParams["lines.linewidth"] = 1
plt.rcParams["lines.markersize"] = 3
image_format = 'png'
image_dpi = 90


def plot_fld(instance, strain_distribution, fracture_forming_limit):
    ffl = 'Data_Layer/%s' % fracture_forming_limit
    ffl = np.genfromtxt(ffl, dtype='float', names=True)
    fig_fld = 'FLD.png'

    ffl_e1 = ffl['e1']
    ffl_e2 = ffl['e2']

    if strain_distribution != '':
        strain = 'Data_Layer/%s/%s' % (instance, strain_distribution)
        print(strain)
        strain = np.genfromtxt(strain, dtype='float', names=True)
        e1 = strain['e1']
        e2 = strain['e2']

    
    # Principal strains distribution in FLD
    fig, ax = plt.subplots()
    ax.plot(ffl_e2, ffl_e1, 'k', label='FFL')
    if strain_distribution != '':
        ax.plot(e2, e1, 'r', label=instance)    
    ax.plot([0,-1], [0,2], 'k--', linewidth=0.5)
    ax.plot([0, 1], [0,1], 'k--', linewidth=0.5)
    ax.plot([0, 0], [0,1], 'k--', linewidth=0.5)
#    title = r'HF-SPIF-1stage, $R$%.0f, $d_0=%0.1f$ mm' % (R, d0)
#    plt.title(title)
    plt.ylabel(r'Major strain, $\varepsilon_1$')
    plt.xlabel(r'Minor strain, $\varepsilon_2$')
    plt.axis([-0.3, 0.3, 0, 1])
    plt.legend()
    
    plt.savefig('Data_Layer/%s/%s' % (instance, fig_fld), dpi=image_dpi, format=image_format)
    plt.show()
    plt.close(fig)
    
    return fig_fld
    




if __name__ == '__main__':
    import os
    os.chdir('../..')
    plot_fld('R6-d635', 'strain.csv', 'files/fracture_forming_limit.csv')
    
