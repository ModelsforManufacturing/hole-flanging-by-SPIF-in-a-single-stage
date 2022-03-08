#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>

Functions to retrieve/save data from/t0 the Data Layer.
"""

import configparser
import shutil       # High-level file operations
import datetime     # Basic date and time types

def retrieve_data(instance):
    """
    Retrieve data from the Data Layer.
    """
    datafile = 'Data_Layer/%s/data.ini' % instance
    parser = configparser.ConfigParser()
    parser.read(datafile)

    blank_d = float(parser.get('Blank Sheet', 'hole diameter'))
    blank_t = float(parser.get('Raw Material', 'thickness'))
    part_d = float(parser.get('Design Part', 'diameter'))
    part_h = float(parser.get('Design Part', 'height'))
    part_3d = parser.get('Design Part', '3d part')
    tool_r = float(parser.get('Forming Tool', 'radius'))
    plastic = parser.get('Plastic behaviour', 'strain-stress curve')
    anisotr = parser.get('Plastic behaviour', 'anisotropy coefficients')
    fracture = parser.get('Fracture behaviour', 'fracture curve')
    stepdown = float(parser.get('Strategy', 'step down'))
    feedrate = float(parser.get('Strategy', 'feedrate'))
    process_3d = parser.get('NC Model', '3d process')
    apt = parser.get('NC Program', 'apt code')
    toolpath = parser.get('Tool Trajectory', 'toolpath code')
    analysis = parser.get('Simulation Model', '3d analysis model')
    sim_strain = parser.get('Simulated Part', 'strain distribution')
    sim_fract = parser.get('Simulated Part', 'fracture location')
    issues_h = float(parser.get('Simulation Issues', 'flange height'))
    manuf_fail = parser.get('Manufactured Part', 'failed')
    manuf_fract = parser.get('Manufactured Part', 'fracture location')
    manuf_h = float(parser.get('Manufactured Part', 'height'))
    manuf_d = float(parser.get('Manufactured Part', 'diameter'))
    manuf_photos = parser.get('Manufactured Part', 'photos')
    analyze_strain = parser.get('Analyzed Part', 'strain distribution')
    analyze_t = parser.get('Analyzed Part', 'thickness profile')
    analyze_fractogr = parser.get('Analyzed Part', 'fractographies')
    manuf_issues_h = float(parser.get('Mahufacturing Issues', 'flange height'))
    
    return blank_d, blank_t, part_d, part_h, part_3d, tool_r, plastic, anisotr, fracture, stepdown, feedrate, process_3d, apt, toolpath, analysis, sim_strain, sim_fract, issues_h, manuf_fail, manuf_fract, manuf_h, manuf_d, manuf_photos, analyze_strain, analyze_t, analyze_fractogr, manuf_issues_h


def save_data(variables, instance):
    """
    Save output data to the Data Layer.
    Previosly, a backup of data.ini is made.
    """
        
    # Backup of 'data.ini'
    datafile = 'Data_Layer/%s/data.ini' % instance
    date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    datafile_backup = 'Data_Layer/%s/data_%s.ini' % (instance, date)
    shutil.copyfile(datafile, datafile_backup)
        
    blank_d, blank_t, part_d, part_h, part_3d, tool_r, plastic, anisotr, fracture, stepdown, feedrate, process_3d, apt, toolpath, analysis, sim_strain, sim_fract, issues_h, manuf_fail, manuf_fract, manuf_h, manuf_d, manuf_photos, analyze_strain, analyze_t, analyze_fractogr, manuf_issues_h = variables

    parser = configparser.ConfigParser()
    parser.add_section('Blank Sheet')
    parser.set('Blank Sheet', 'hole diameter', '%s' % blank_d)
    parser.add_section('Raw Material')
    parser.set('Raw Material', 'thickness', '%s' % blank_t)
    parser.add_section('Design Part')
    parser.set('Design Part', 'diameter', '%s' % part_d)
    parser.set('Design Part', 'height', '%s' % part_h)
    parser.set('Design Part', '3d part', '%s' % part_3d)
    parser.add_section('Forming Tool')
    parser.set('Forming Tool', 'radius', '%s' % tool_r)
    parser.add_section('Plastic behaviour')
    parser.set('Plastic behaviour', 'strain-stress curve', '%s' % plastic)
    parser.set('Plastic behaviour', 'anisotropy coefficients', '%s' % anisotr)
    parser.add_section('Fracture behaviour')
    parser.set('Fracture behaviour', 'fracture curve', '%s' % fracture)
    parser.add_section('Strategy')
    parser.set('Strategy', 'step down', '%s' % stepdown)
    parser.set('Strategy', 'feedrate', '%s' % feedrate)
    parser.add_section('NC Model')
    parser.set('NC Model', '3d process', '%s' % process_3d)
    parser.add_section('NC Program')
    parser.set('NC Program', 'apt code', '%s' % apt)
    parser.add_section('Tool Trajectory')
    parser.set('Tool Trajectory', 'toolpath code', '%s' % toolpath)
    parser.add_section('Simulation Model')
    parser.set('Simulation Model', '3d analysis model', '%s' % analysis)
    parser.add_section('Simulated Part')
    parser.set('Simulated Part', 'strain distribution', '%s' % sim_strain)
    parser.set('Simulated Part', 'fracture location', '%s' % sim_fract)
    parser.add_section('Simulation Issues')
    parser.set('Simulation Issues', 'flange height', '%s' % issues_h)
    parser.add_section('Manufactured Part')
    parser.set('Manufactured Part', 'failed', '%s' % manuf_fail)
    parser.set('Manufactured Part', 'fracture location', '%s' % manuf_fract)
    parser.set('Manufactured Part', 'height', '%s' % manuf_h)
    parser.set('Manufactured Part', 'diameter', '%s' % manuf_d)
    parser.set('Manufactured Part', 'photos', '%s' % manuf_photos)
    parser.add_section('Analyzed Part')
    parser.set('Analyzed Part', 'strain distribution', '%s' % analyze_strain)
    parser.set('Analyzed Part', 'thickness profile', '%s' % analyze_t)
    parser.set('Analyzed Part', 'fractographies', '%s' % analyze_fractogr)
    parser.add_section('Mahufacturing Issues')
    parser.set('Mahufacturing Issues', 'flange height', '%s' % manuf_issues_h)

    with open(datafile, 'w') as configfile:
        parser.write(configfile)


    
if __name__ == '__main__':
    variables = retrieve_data('instance01')
    print(variables)
    save_data(variables, 'instance01')

