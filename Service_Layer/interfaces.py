#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>

This module implements all functions defined in interfaces/interfaces_service.py.

"""

import Service_Layer.extra as extra

def calculate_flange_height(instance, t0, d0, R, df):
    '''
    Simple estimation for the final flange height.
    '''
    h = (df - d0)/2
    print('Calculating flange height:')
    print('   t0 = %f mm, d0 = %f mm, R = %f mm, df = %f mm' % (t0, d0, R, df))
    print('   Output: flange height = %f mm' % h)
    return h

def calculate_tool_path(instance, t0, df, h, R, f, sd):
#    toolpath_code = "this is a test: toolpath_code"
    print('Generating toolpath code:')
    print('   t0 = %f mm, df = %f mm, h = %f mm, R = %f mm, f = %f mm/min, sd = %f mm' % (t0, df, h, R, f, sd))
    
    import Service_Layer.toolpath_SPIF_helix.toolpath_helix as tp
    filename = tp.toolpath_helix(instance, R, h, df, f, sd)
    
    print('   Output: tool path in file "%s"' % filename)
    return filename

def generate_g_code(instance, toolpath):
    g_code = "nc-program.gcode"
    print('Generating G-code:')
    print('   tool path in file "%s"' % toolpath)
    print('   Output: G-code in file "%s"' % g_code)
    return g_code

def prepare_specimen(instance, t0, d0, g_code):
    if g_code == '':
        print('Warning: the G-code is required before executing this action.')
        is_prepared = ''
    else:
        print('To perform the experimental test, a specimen is required with a %f-mm sheet thickness and a %f-mm hole diameter.' % (t0, d0))
        is_prepared = input('Has the specimen already been manufactured? ')
        is_prepared = is_prepared.lower()
        if is_prepared in ['yes', 'y']:
            print('Ok, task completed.')
        elif is_prepared in ['no', 'n']:
            print('Ok. Please note that this task has not been completed yet.')
        else:
            print('Answer not valid.')
            is_prepared = ''
    return is_prepared

def perform_hole_flanging_test(instance, is_prepared, gcode):
    if not is_prepared in ['yes', 'y']:
        print('Warning: the specimen has not been prepared yet.')
        is_fractured = ''
    else:
        print('Use the prepared speciment to perform an experimental hole flanging test.')
        print('G-code: %s' % gcode)
        print("Enter Yes or No if the speciment has fractured or not, respectively. Enter anything else if the experiment hasn't been done yet.")
        is_fractured = input('Is the specimen fractured (Yes/No)? ')
        is_fractured = is_fractured.lower()
        if is_fractured in ['yes', 'y', 'no', 'n']:
            print('Ok, task completed.')
        else:
            print('Ok. Please note that this task has not been completed yet.')
            is_fractured = ''
    return is_fractured

def measure_flange_height(instance, is_fractured):
    if not is_fractured in ['yes', 'y', 'no', 'n']:
        print('Wait, wait... was the specimen fractured or not?')
        h = 0
    elif is_fractured in ['yes', 'y']:
        print('Flange height cannot be measured for a fractured specimen.')
        h = 0
    else: # is_fractured == "no"
        h = float(input('Enter the measured flange height (mm): '))
    return h

def measure_strain_distribution(instance, is_fractured):
    strain = ''
    if not is_fractured in ['yes', 'y', 'no', 'n']:
        print('Wait, wait... was the specimen fractured or not?')
    else: # is_fractured == "no" or "yes"
        print('Use ARGUS to obtain the strain distribution along the flange.')
        print('Save the results as a text file "strain.csv" and upload it to "Data_Layer/%s".' % instance)
        q = input('Is the file already uploaded? (Yes/No) ')
        q = q.lower()
        if q in ['yes', 'y']:
            strain = 'strain.csv'
    return strain

def calculate_hole_expansion_ratio(instance, d0, df, is_fractured):
    if not is_fractured in ['no', 'n']:
        print('Warning: this task can only be executed for non fractured specimens.')
        her = 0
    else:
        print('Calculating HER...')
        her = d0/df
        print('    Output: HER = d0/df = %f' % her)
    return her

def calculate_non_dimensional_flange_height(instance, df, is_fractured, h):
    if not is_fractured in ['no', 'n']:
        print('Ups! h/df can be only calculated if the specimen was no fractured')
        h_df = 0
    else:
        print('Calculating h/df...')
        h_df = h/df
        print('    Output: h/df = %f' % h_df)
    return h_df

def calculate_non_dimensional_average_thickness(instance, d0, t0, df, is_fractured, h):
    if not is_fractured in ['no', 'n']:
        print('Ups! t/t0 can be only calculated if the specimen was no fractured')
        t_t0 = 0
    else:
        print('Calculating t/t0...')
        t = t0*(df-d0)/2/h                      # only for test purposes
        t_t0 = t/t0
        print('    Output: t/t0 = %f' % t_t0)
    return t_t0

def calculate_global_lfr(instance, her, is_fracture):
    # search in all succesful tests and calculate LFR=max(HER)
    global_lfr = extra.calculate_global_lfr(her, is_fracture)
    return global_lfr

def calculate_lfr_per_tool(instance, her, is_fracture, R):
    # search in all succesful tests using tool radius R and calculate LFR=max(HER)
    lfr_per_tool = extra.calculate_lfr_per_tool(her, is_fracture, R)
    return lfr_per_tool

def plot_global_fld(instance, strain_distribution, fracture_forming_limit):
    global_fld = extra.plot_global_fld(instance, strain_distribution, fracture_forming_limit)
    return global_fld
    
def plot_fld_per_tool(instance, strain_distribution, fracture_forming_limit, R):
    # TODO
    fld_per_tool = 'TBD'
    return fld_per_tool

def plot_fld_for_successful_tests(instance, strain_distribution, fracture_forming_limit, is_fractured):
    # TODO
    fld_for_successful_tests = 'TBD'
    return fld_for_successful_tests

def plot_fld_for_fractured_tests(instance, strain_distribution, fracture_forming_limit, is_fractured):
    # TODO
    fld_for_fractured_tests = 'TBD'
    return fld_for_fractured_tests

def plot_h_df(instance, h_df):
    # TODO
    flange_height_diagram = 'TBD'
    return flange_height_diagram

def plot_t_t0(instance, t_t0):
    # TODO
    average_thickness_diagram = 'TBD'
    return average_thickness_diagram

def conclusions_for_lfr(instance, global_lfr, lfr_per_tool):
    # TODO
    print('LFR = %f' % global_lfr)
    print('LFR per tool = %f' % lfr_per_tool)
    conclusions_limit_forming_ratio = 'TBD'
    return conclusions_limit_forming_ratio
    
def conclusions_for_height(instance, flange_height_diagram):
    # TODO
    conclusions_flange_height = 'TBD'
    return conclusions_flange_height
    
def conclusions_for_thickness(instance, average_thickness_diagram):
    # TODO
    conclusions_average_thickness = 'TBD'
    return conclusions_average_thickness
    
def conclusions_for_t0_r(instance, global_lfr, lfr_per_tool, global_fld, fld_per_tool, fld_for_successful_tests, fld_for_fractured_tests, flange_height_diagram, average_thickness_diagram):
    # TODO
    conclusions_bending_ratio = 'TBD'
    return conclusions_bending_ratio
    
    
