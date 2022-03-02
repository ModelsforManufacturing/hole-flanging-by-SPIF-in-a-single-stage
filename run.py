#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>

"""

import Data_Layer.interfaces as data
import Service_Layer.interfaces as service

def _retrieve_variables(datafile):
    variables = data.retrieve_data(datafile)
    return variables

def _save_variables(variables, datafile):
    data.save_data(variables, datafile)

def a11_t1_calculate_flange_height(datafileinput, datafileoutput):
    """
    Activity: A11 Update Design Part
    Task: T1 Calculate flange height
    """
    blank_d, blank_t, part_d, part_h, part_tol, part_3d, tool_r, issues_h = _retrieve_variables(datafileinput)

    part_h = service.calculate_flange_height(blank_d, part_d, issues_h)

    variables = (blank_d, blank_t, part_d, part_h, part_tol, part_3d, tool_r, issues_h)
    _save_variables(variables, datafileoutput)
    
    return part_h

def a11_t2_update_cad_model(datafileinput, datafileoutput):
    """
    A11 Update Design Part
    T2 Generate CAD Model
    """
    blank_d, blank_t, part_d, part_h, part_tol, part_3d, tool_r, issues_h = _retrieve_variables(datafileinput)

    part_3d = service.generate_cad_model(blank_d, part_d, part_h, part_3d)

    variables = (blank_d, blank_t, part_d, part_h, part_tol, part_3d, tool_r, issues_h)
    _save_variables(variables, datafileoutput)
    
    return part_3d


if __name__ == '__main__':
    print('Starting... ')
    input("Press Enter to continue")

    print('A11 Update Design Part: T1 Calculate flange height')
    h = a11_t1_calculate_flange_height('Data_Layer/instance01.ini', 'Data_Layer/instance01_A11_T1.ini')
    print('   flange height = %f mm' % h)
    input("Press Enter to continue")

    print('A11 Update Design Part: T2 Generate CAD Model')
    part3d = a11_t2_update_cad_model('Data_Layer/instance01_A11_T1.ini', 'Data_Layer/instance01_A11_T2.ini')
    print('   part 3d model = %s' % part3d)
    input("Press Enter to continue")
    
