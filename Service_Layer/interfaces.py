#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>

Functions to implement the Behaviour Model.

There is a function for each 'Task' of the 'Elementary Activities'.

Format:

def <task>(<input_1>, ...(<input_n>):
    ''' <rule> '''
    if <constraint>:
        <action>
    else:
        <action>
    return (<output_1>, ...<output_n>)

"""


"""
A11 Update Design Part
"""

def calculate_flange_height(blank_d, part_d, simul_issues_h):
    '''
    Update the flange height according to an equation.
    The equation has been defined as a Python function.
    Import and run the Python function.
    '''
    
    from Service_Layer.actions.a11_t1_flange_height import flange_height
    part_h = flange_height(part_d, blank_d)
    
    if not part_h > simul_issues_h:
    
        from Service_Layer.actions.a11_t1_flange_height import alternative_flange_height
        part_h = alternative_flange_height(part_d, blank_d, simul_issues_h)
        
    return part_h


def generate_cad_model(blank_d, part_d, part_h, part_3d_model):
    '''
    Update a parametrized CAD model with the actual parameters.
    The CAD model is a CATPart file that can be updated with a CATIA macro script.
    Run the CATIA macro script.
    '''

    '''
    TODO: see https://stackoverflow.com/questions/34833407/run-a-catia-macro-with-a-python-script#36212094
    import win32com.client
    catapp = win32com.client.Dispatch('CATIA.Application')
    catapp.StartCommand('Service_Layer/actions/a11_t2_part_3d_model.CATScript')
    '''
    
    return part_3d_model
    

"""
A12 Generate NC
"""

def create_NC_model(part_3d_model, tool_radius, stepdown, feedrate):
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



