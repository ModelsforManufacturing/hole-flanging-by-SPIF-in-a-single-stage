#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Domingo Morales Palma <dmpalma@us.es>

Functions to retrieve/save data from/to the Data Layer.

This file has been generated automatically.
'''

import configparser # Configuration file parser
import shutil       # High-level file operations
import datetime     # Basic date and time types
from interfaces.data_classes import *


class Instance:
    '''
    '''
    def __init__(self, instance_name):
        '''
        Creates a Instance object with data from a `data.ini` file.
        
        Keyword arguments:
        instance_name -- string
        '''
        self.instance_name = instance_name

        datafile = 'Data_Layer/%s/data.ini' % instance_name
        self.datafile = datafile
        
        parser = configparser.ConfigParser()
        parser.read(datafile)
        thickness_1 = float(parser.get('Blank Model', 'thickness'))
        hole_diameter_2 = float(parser.get('Blank Model', 'hole diameter'))
        diameter_3 = float(parser.get('Part Model', 'diameter'))
        flange_height_4 = float(parser.get('Part Model', 'flange height'))
        radius_5 = float(parser.get('Forming Tool Model', 'radius'))
        toolpath_code_6 = parser.get('Tool Path', 'toolpath code')
        feed_rate_7 = float(parser.get('Forming Conditions', 'feed rate'))
        step_down_8 = float(parser.get('Forming Conditions', 'step down'))
        g_code_9 = parser.get('NC Program', 'g-code')
        is_prepared_10 = parser.get('Specimen', 'is prepared')
        is_fractured_11 = parser.get('Test Results', 'is fractured')
        flange_height_12 = float(parser.get('Test Results', 'flange height'))
        strain_distribution_13 = parser.get('Test Results', 'strain distribution')
        hole_expansion_ratio_14 = float(parser.get('Test Results', 'hole expansion ratio'))
        non_dimensional_flange_height_15 = float(parser.get('Test Results', 'non-dimensional flange height'))
        non_dimensional_average_thickness_16 = float(parser.get('Test Results', 'non-dimensional average thickness'))
        fracture_forming_limit_17 = parser.get('Material Properties', 'fracture forming limit')
        global_lfr_18 = float(parser.get('LFR', 'global lfr'))
        lfr_per_tool_19 = float(parser.get('LFR', 'lfr per tool'))
        global_fld_20 = parser.get('FLD', 'global fld')
        fld_per_tool_21 = parser.get('FLD', 'fld per tool')
        fld_for_successful_tests_22 = parser.get('FLD', 'fld for successful tests')
        fld_for_fractured_tests_23 = parser.get('FLD', 'fld for fractured tests')
        flange_height_diagram_24 = parser.get('Technological Parameters', 'flange height diagram')
        average_thickness_diagram_25 = parser.get('Technological Parameters', 'average thickness diagram')
        limit_forming_ratio_26 = parser.get('Conclusions', 'limit forming ratio')
        flange_height_27 = parser.get('Conclusions', 'flange height')
        average_thickness_28 = parser.get('Conclusions', 'average thickness')
        bending_ratio_29 = parser.get('Conclusions', 'bending ratio')


        self.blank_model = BlankModel(thickness_1, hole_diameter_2)
        self.part_model = PartModel(diameter_3, flange_height_4)
        self.forming_tool_model = FormingToolModel(radius_5)
        self.tool_path = ToolPath(toolpath_code_6)
        self.forming_conditions = FormingConditions(feed_rate_7, step_down_8)
        self.nc_program = NcProgram(g_code_9)
        self.specimen = Specimen(is_prepared_10)
        self.test_results = TestResults(is_fractured_11, flange_height_12, strain_distribution_13, hole_expansion_ratio_14, non_dimensional_flange_height_15, non_dimensional_average_thickness_16)
        self.material_properties = MaterialProperties(fracture_forming_limit_17)
        self.analysis_results = AnalysisResults()
        self.lfr = Lfr(global_lfr_18, lfr_per_tool_19)
        self.fld = Fld(global_fld_20, fld_per_tool_21, fld_for_successful_tests_22, fld_for_fractured_tests_23)
        self.technological_parameters = TechnologicalParameters(flange_height_diagram_24, average_thickness_diagram_25)
        self.conclusions = Conclusions(limit_forming_ratio_26, flange_height_27, average_thickness_28, bending_ratio_29)


    def save(self):
        '''
        Make a backup copy of `data.ini` before saving the data.
        '''
        # Backup of 'data.ini'
        date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        datafile_backup = 'Data_Layer/%s/data_%s.ini' % (self.instance_name, date)
        shutil.copyfile(self.datafile, datafile_backup)

        config = configparser.ConfigParser()
        config['Blank Model'] = {
            'thickness': self.blank_model.thickness,
            'hole diameter': self.blank_model.hole_diameter,
        }
        config['Part Model'] = {
            'diameter': self.part_model.diameter,
            'flange height': self.part_model.flange_height,
        }
        config['Forming Tool Model'] = {
            'radius': self.forming_tool_model.radius,
        }
        config['Tool Path'] = {
            'toolpath code': self.tool_path.toolpath_code,
        }
        config['Forming Conditions'] = {
            'feed rate': self.forming_conditions.feed_rate,
            'step down': self.forming_conditions.step_down,
        }
        config['NC Program'] = {
            'g-code': self.nc_program.g_code,
        }
        config['Specimen'] = {
            'is prepared': self.specimen.is_prepared,
        }
        config['Test Results'] = {
            'is fractured': self.test_results.is_fractured,
            'flange height': self.test_results.flange_height,
            'strain distribution': self.test_results.strain_distribution,
            'hole expansion ratio': self.test_results.hole_expansion_ratio,
            'non-dimensional flange height': self.test_results.non_dimensional_flange_height,
            'non-dimensional average thickness': self.test_results.non_dimensional_average_thickness,
        }
        config['Material Properties'] = {
            'fracture forming limit': self.material_properties.fracture_forming_limit,
        }
        config['Analysis Results'] = {
        }
        config['LFR'] = {
            'global lfr': self.lfr.global_lfr,
            'lfr per tool': self.lfr.lfr_per_tool,
        }
        config['FLD'] = {
            'global fld': self.fld.global_fld,
            'fld per tool': self.fld.fld_per_tool,
            'fld for successful tests': self.fld.fld_for_successful_tests,
            'fld for fractured tests': self.fld.fld_for_fractured_tests,
        }
        config['Technological Parameters'] = {
            'flange height diagram': self.technological_parameters.flange_height_diagram,
            'average thickness diagram': self.technological_parameters.average_thickness_diagram,
        }
        config['Conclusions'] = {
            'limit forming ratio': self.conclusions.limit_forming_ratio,
            'flange height': self.conclusions.flange_height,
            'average thickness': self.conclusions.average_thickness,
            'bending ratio': self.conclusions.bending_ratio,
        }

        
        with open(self.datafile, 'w') as configfile:
            config.write(configfile)
    
