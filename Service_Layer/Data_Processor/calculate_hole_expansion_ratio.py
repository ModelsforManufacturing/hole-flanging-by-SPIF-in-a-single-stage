#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>
"""

def calculate_hole_expansion_ratio(d0, df):
    her = df/d0
    return her

if __name__ == '__main__':
    d0 = 58
    df = 95.8
    her = calculate_hole_expansion_ratio(d0, df)
    print("Returned her = %f" % her)
