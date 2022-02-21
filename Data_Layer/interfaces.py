#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>

Functions to retrieve/save data from/t0 the Data Layer.
"""

import configparser

def retrieve_data(datafile):
    """
    Retrieve data from the Data Layer.
    Example of datafile: 'example_01.ini'
    """
    parser = configparser.SafeConfigParser()
    parser.read(datafile)

    blank_d = float(parser.get('Blank Sheet', 'hole diameter'))
    blank_t = float(parser.get('Raw Material', 'thickness'))
    part_d = float(parser.get('Design Part', 'diameter'))
    part_h = float(parser.get('Design Part', 'height'))
    part_tol = float(parser.get('Design Part', 'tolerance'))
    part_3d = string(parser.get('Design Part', '3d part'))
    tool_r = string(parser.get('Forming Tool', 'radius'))
    
    variables = (blank_d, blank_t, part_d, part_h, part_tol, part_3d, tool_r)
    
    return variables

def save_data(variables, datafile):
    """
    Save output data to the Data Layer.
    Save all data to another file and trace life cycle of files.
    File name format: <instance_name>_A<activity_number>_T<task_number>.ini
    Example: 'example_01_A11_T1.ini'
    """
    blank_d, blank_t, part_d, part_h, part_tol, part_3d, tool_r = variables

    parser = configparser.SafeConfigParser()
    parser.add_section('Blank Sheet')
    parser.set('Blank Sheet', 'hole diameter', '%s' % blank_d))
    parser.add_section('Raw Material')
    parser.set('Raw Material', 'thickness', '%s' % blank_t))
    parser.add_section('Design Part')
    parser.set('Design Part', 'diameter', '%s' % part_d))
    parser.set('Design Part', 'height', '%s' % part_h))
    parser.set('Design Part', 'tolerance', '%s' % part_tol))
    parser.set('Design Part', '3d part', '%s' % part_3d))
    parser.add_section('Forming Tool')
    parser.set('Forming Tool', 'radius', '%s' % tool_r))

    parser.write(datafile)


    

