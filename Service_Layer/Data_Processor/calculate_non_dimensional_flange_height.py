#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>
"""

def calculate_non_dimensional_flange_height(h, df):
    h_df = h/df
    return h_df

if __name__ == '__main__':
    h = 24
    df = 95.8
    h_df = calculate_non_dimensional_flange_height(h, df)
    print("Returned h_df = %f" % h_df)
