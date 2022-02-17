#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>

Functions to implement the Behaviour Model.

There is a function for each 'Task' of the 'Elementary Activities'.

Format:

def <task>(<input_1>, ...(<inputn_>):
    ''' <rule> '''
    ...
    return (<output_1>, ...<output_n>)

"""


"""
A11 Update Design Part
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
    

"""
A12 Generate NC
"""

def create_NC_model(part, radius, stepdown, feedrate):
    ''' Update a parametrized NC model with the actual parameters '''
    return process

def simulate_NC_model(process):
    ''' Analyse tool path to avoid tool collisions '''
    return process

def generate_NC_code(process):
    ''' Generate and export the APT code '''
    return apt_code


"""
A21 Extract Tool Trajectory
"""


"""
A22 Simulate SPIF Process
"""


"""
A23 Validate Simulation
"""


"""
A24 Analyze Simulation
"""


"""
A3 Inspect Manufactured Part
"""



