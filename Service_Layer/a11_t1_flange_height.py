#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>

"""

def flange_height(part_diameter, blank_hole_diameter):
    '''
    A simple estimation for the final flange height of the design part.
    '''
    return (part_diameter - blank_hole_diameter)/2
    
def alternative_flange_height(part_diameter, blank_hole_diameter, simulated_flange_height):
    '''
    A simple correction for the final flange height of the design part given the flange height obtained in the numerical simulation.
    '''
    return simulated_flange_height
    
