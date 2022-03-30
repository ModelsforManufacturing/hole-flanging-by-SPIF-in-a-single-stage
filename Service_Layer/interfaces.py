#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>

This module implements all functions defined in interfaces/interfaces_service.py.

"""

def calculate_flange_height(df, d0, h_issues):
    '''
    It calculates a simple estimation for the final flange height of the design part.
    If simulation predicts an insuficcient height, an alternative value is returned instead.
    '''
    h = (df - d0)/2
    if h > h_issues:
        return h
    else:
        return h_issues


def generate_cad_model(df, d0, h, model):
    pass
    
    
def extract_tool_movements(apt_file):
    import io
    filename = 'Data_Layer/files/%s' % apt_file
    f = open(filename, 'r')
    apt = f.read()
    f.close()
    from Service_Layer.a21_t1_extract_tool_movements import apt2toolpath
    feedrate_x_y_z = apt2toolpath(apt)
    return feedrate_x_y_z
    
    
def calculate_path_lengths_and_times(feedrate_x_y_z):
    feedrate_x_y_z = extract_tool_movements('CATIA/HF1-D58-R10_Hole-Flanging_Tool_R10.aptsource') ######## TODO

    from Service_Layer.a21_t2_calculate_path_lengths_and_times import toolpath2time
    time_x_y_z = toolpath2time(feedrate_x_y_z)
    return time_x_y_z
    
    
def write_results(time_x_y_z):
    feedrate_x_y_z = extract_tool_movements('CATIA/HF1-D58-R10_Hole-Flanging_Tool_R10.aptsource') ######## TODO
    time_x_y_z = calculate_path_lengths_and_times(feedrate_x_y_z)

    from Service_Layer.a21_t3_write_results import create_toolpath_files_for_abaqus
    directory='Data_Layer/instance01/' ######## TODO
    toolpath_files = create_toolpath_files_for_abaqus(time_x_y_z, directory)
    res = [i.replace(directory, '') for i in toolpath_files]
    toolpath_code = '(%s, %s, %s, %s)' % (res[0], res[1], res[2], res[3])
    return toolpath_code
    
    
def create_nc_model(part, r, sd, f):
    pass
    
    
def simulate_nc_model(process):
    pass
    
    

