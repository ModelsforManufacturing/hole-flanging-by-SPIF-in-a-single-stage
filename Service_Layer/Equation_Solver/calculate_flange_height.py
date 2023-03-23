#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>
"""

def calculate_flange_height(t0, d0, R, df):
    '''
    Simple estimation for the final flange height.
    '''
#    print('Calculating flange height:')
#    print('   t0 = %f mm, d0 = %f mm, R = %f mm, df = %f mm' % (t0, d0, R, df))
    h = (df - d0)/2
#    print('   flange height = %.2f mm' % h)
    return h


if __name__ == '__main__':
    t0 = 1.6
    d0 = 58
    R = 8
    df = 95.8
    h = calculate_flange_height(t0, d0, R, df)
    print('h = %f mm' % h)
