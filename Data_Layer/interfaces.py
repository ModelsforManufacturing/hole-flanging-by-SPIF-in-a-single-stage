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
    Example of datafile: 'instance01.ini'
    """
    parser = configparser.ConfigParser()
    parser.read(datafile)

    blank_d = float(parser.get('Blank Sheet', 'hole diameter'))
    blank_t = float(parser.get('Raw Material', 'thickness'))
    part_d = float(parser.get('Design Part', 'diameter'))
    part_h = float(parser.get('Design Part', 'height'))
    part_tol = float(parser.get('Design Part', 'tolerance'))
    part_3d = parser.get('Design Part', '3d part')
    tool_r = float(parser.get('Forming Tool', 'radius'))
    issues_h = float(parser.get('Simulation Issues', 'flange height'))
    
    return blank_d, blank_t, part_d, part_h, part_tol, part_3d, tool_r, issues_h


def save_data(variables, datafile):
    """
    Save output data to the Data Layer.
    Save all data to another file and trace life cycle of files.
    File name format: <instance_name>_A<activity_number>_T<task_number>.ini
    Example: 'instance01_A11_T1.ini'
    """
    blank_d, blank_t, part_d, part_h, part_tol, part_3d, tool_r, issues_h = variables

    parser = configparser.ConfigParser()
    parser.add_section('Blank Sheet')
    parser.set('Blank Sheet', 'hole diameter', '%s' % blank_d)
    parser.add_section('Raw Material')
    parser.set('Raw Material', 'thickness', '%s' % blank_t)
    parser.add_section('Design Part')
    parser.set('Design Part', 'diameter', '%s' % part_d)
    parser.set('Design Part', 'height', '%s' % part_h)
    parser.set('Design Part', 'tolerance', '%s' % part_tol)
    parser.set('Design Part', '3d part', '%s' % part_3d)
    parser.add_section('Forming Tool')
    parser.set('Forming Tool', 'radius', '%s' % tool_r)
    parser.add_section('Simulation Issues')
    parser.set('Simulation Issues', 'flange height', '%s' % issues_h)

    with open(datafile, 'w') as configfile:
        parser.write(configfile)


    
if __name__ == '__main__':
    variables = retrieve_data('Data_Layer/instance01.ini')
    print(variables)
    save_data(variables, 'Data_Layer/instance01_output.ini')

