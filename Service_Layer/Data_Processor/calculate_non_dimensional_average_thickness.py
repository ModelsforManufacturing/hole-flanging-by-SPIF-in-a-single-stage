#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>
"""

def calculate_non_dimensional_average_thickness(t0, d0, df, h):
    t = t0*(df-d0)/2/h      # only for test purposes
    t_t0 = t/t0
    return t_t0

if __name__ == '__main__':
    t0 = 1.6
    d0 = 58
    df = 95.8
    h = 24
    t_t0 = calculate_non_dimensional_average_thickness(t0, d0, df, h)
    print("Returned t_t0 = %f" % t_t0)
