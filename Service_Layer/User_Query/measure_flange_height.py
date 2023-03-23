#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>
"""

def measure_flange_height():
    h = float(input('Enter the measured flange height (mm): '))
    return h

if __name__ == '__main__':
    h = measure_flange_height()
    print("Returned h = %f" % h)
