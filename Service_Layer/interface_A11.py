#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>
"""

def calculate_flange_height(blank_d, part_d, part_h, simul_issues_h):
    ''' Update the flange height according to an equation '''
    if !simul_issues_h or part_h == 0:
        part_h = (part_d - blank_d)/2
    else:
        part_h = simul_issues_h     # increase flange height
    return part_h

def generate_cad_model(blank_d, part_d, part_h):
    ''' Update a parametrized CAD model with the actual parameters '''
    return 0
    

