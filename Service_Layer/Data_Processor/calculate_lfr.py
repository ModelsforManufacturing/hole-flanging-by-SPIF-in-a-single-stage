#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>
"""

def calculate_lfr(her_list):
    lfr = max(her_list)    
    return lfr

if __name__ == '__main__':
    her_list = [
        1.35,
        2.34,
        4.2,
        0.12]
    lfr = calculate_lfr(her_list)

    print('HER = %s' % her_list)
    print('LFR = %s' % lfr)
    print("Returned lfr = %f" % lfr)
