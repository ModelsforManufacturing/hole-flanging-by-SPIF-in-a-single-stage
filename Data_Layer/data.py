#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Domingo Morales Palma <dmpalma@us.es>

Functions to retrieve/save data from/to the Data Layer.

Implementation of all interfaces:
    <Class>Interface
in module:
    interfaces.data_interface

This file has been generated automatically.
'''

import os           # Miscellaneous operating system interfaces
import configparser # Configuration file parser
import shutil       # High-level file operations
import datetime     # Basic date and time types

class AnalysisResults:
    def __init__(self, ):
        pass
    def load(self, instance_name):
        i = DataInstance(instance_name)
        i.load()

    def save(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        i.save()

class NcProgram:
    def __init__(self, g_code):
        self.g_code = g_code

    def load(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        self.g_code = i.nc_program.g_code

    def save(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        i.nc_program.g_code = self.g_code
        i.save()

class PartModel:
    def __init__(self, diameter, flange_height):
        self.diameter = diameter
        self.flange_height = flange_height

    def load(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        self.diameter = i.part_model.diameter
        self.flange_height = i.part_model.flange_height

    def save(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        i.part_model.diameter = self.diameter
        i.part_model.flange_height = self.flange_height
        i.save()

class FormingToolModel:
    def __init__(self, radius):
        self.radius = radius

    def load(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        self.radius = i.forming_tool_model.radius

    def save(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        i.forming_tool_model.radius = self.radius
        i.save()

class MaterialProperties:
    def __init__(self, fracture_forming_limit):
        self.fracture_forming_limit = fracture_forming_limit

    def load(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        self.fracture_forming_limit = i.material_properties.fracture_forming_limit

    def save(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        i.material_properties.fracture_forming_limit = self.fracture_forming_limit
        i.save()

class BlankModel:
    def __init__(self, thickness, hole_diameter):
        self.thickness = thickness
        self.hole_diameter = hole_diameter

    def load(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        self.thickness = i.blank_model.thickness
        self.hole_diameter = i.blank_model.hole_diameter

    def save(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        i.blank_model.thickness = self.thickness
        i.blank_model.hole_diameter = self.hole_diameter
        i.save()

class Conclusions:
    def __init__(self, limit_forming_ratio, flange_height, average_thickness, bending_ratio):
        self.limit_forming_ratio = limit_forming_ratio
        self.flange_height = flange_height
        self.average_thickness = average_thickness
        self.bending_ratio = bending_ratio

    def load(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        self.limit_forming_ratio = i.conclusions.limit_forming_ratio
        self.flange_height = i.conclusions.flange_height
        self.average_thickness = i.conclusions.average_thickness
        self.bending_ratio = i.conclusions.bending_ratio

    def save(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        i.conclusions.limit_forming_ratio = self.limit_forming_ratio
        i.conclusions.flange_height = self.flange_height
        i.conclusions.average_thickness = self.average_thickness
        i.conclusions.bending_ratio = self.bending_ratio
        i.save()

class ToolPath:
    def __init__(self, toolpath_code):
        self.toolpath_code = toolpath_code

    def load(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        self.toolpath_code = i.tool_path.toolpath_code

    def save(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        i.tool_path.toolpath_code = self.toolpath_code
        i.save()

class Specimen:
    def __init__(self, is_prepared):
        self.is_prepared = is_prepared

    def load(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        self.is_prepared = i.specimen.is_prepared

    def save(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        i.specimen.is_prepared = self.is_prepared
        i.save()

class FormingConditions:
    def __init__(self, feed_rate, step_down):
        self.feed_rate = feed_rate
        self.step_down = step_down

    def load(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        self.feed_rate = i.forming_conditions.feed_rate
        self.step_down = i.forming_conditions.step_down

    def save(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        i.forming_conditions.feed_rate = self.feed_rate
        i.forming_conditions.step_down = self.step_down
        i.save()

class Fld:
    def __init__(self, global_fld, fld_per_tool, fld_for_successful_tests, fld_for_fractured_tests):
        self.global_fld = global_fld
        self.fld_per_tool = fld_per_tool
        self.fld_for_successful_tests = fld_for_successful_tests
        self.fld_for_fractured_tests = fld_for_fractured_tests

    def load(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        self.global_fld = i.fld.global_fld
        self.fld_per_tool = i.fld.fld_per_tool
        self.fld_for_successful_tests = i.fld.fld_for_successful_tests
        self.fld_for_fractured_tests = i.fld.fld_for_fractured_tests

    def save(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        i.fld.global_fld = self.global_fld
        i.fld.fld_per_tool = self.fld_per_tool
        i.fld.fld_for_successful_tests = self.fld_for_successful_tests
        i.fld.fld_for_fractured_tests = self.fld_for_fractured_tests
        i.save()

class TechnologicalParameters:
    def __init__(self, flange_height_diagram, average_thickness_diagram):
        self.flange_height_diagram = flange_height_diagram
        self.average_thickness_diagram = average_thickness_diagram

    def load(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        self.flange_height_diagram = i.technological_parameters.flange_height_diagram
        self.average_thickness_diagram = i.technological_parameters.average_thickness_diagram

    def save(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        i.technological_parameters.flange_height_diagram = self.flange_height_diagram
        i.technological_parameters.average_thickness_diagram = self.average_thickness_diagram
        i.save()

class TestResults:
    def __init__(self, is_fractured, flange_height, strain_distribution, hole_expansion_ratio, non_dimensional_flange_height, non_dimensional_average_thickness):
        self.is_fractured = is_fractured
        self.flange_height = flange_height
        self.strain_distribution = strain_distribution
        self.hole_expansion_ratio = hole_expansion_ratio
        self.non_dimensional_flange_height = non_dimensional_flange_height
        self.non_dimensional_average_thickness = non_dimensional_average_thickness

    def load(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        self.is_fractured = i.test_results.is_fractured
        self.flange_height = i.test_results.flange_height
        self.strain_distribution = i.test_results.strain_distribution
        self.hole_expansion_ratio = i.test_results.hole_expansion_ratio
        self.non_dimensional_flange_height = i.test_results.non_dimensional_flange_height
        self.non_dimensional_average_thickness = i.test_results.non_dimensional_average_thickness

    def save(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        i.test_results.is_fractured = self.is_fractured
        i.test_results.flange_height = self.flange_height
        i.test_results.strain_distribution = self.strain_distribution
        i.test_results.hole_expansion_ratio = self.hole_expansion_ratio
        i.test_results.non_dimensional_flange_height = self.non_dimensional_flange_height
        i.test_results.non_dimensional_average_thickness = self.non_dimensional_average_thickness
        i.save()

class Lfr:
    def __init__(self, global_lfr, lfr_per_tool):
        self.global_lfr = global_lfr
        self.lfr_per_tool = lfr_per_tool

    def load(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        self.global_lfr = i.lfr.global_lfr
        self.lfr_per_tool = i.lfr.lfr_per_tool

    def save(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        i.lfr.global_lfr = self.global_lfr
        i.lfr.lfr_per_tool = self.lfr_per_tool
        i.save()



class DataInstance:
    '''
    '''
    def __init__(self, instance_name):
        '''
        Creates a DataInstance object with 2 parameters:
        instance_name -- string
        datafile -- string
        '''
        self.instance_name = instance_name
        self.datafile = 'Data_Layer/%s/data.ini' % instance_name
        

    def new(self):
        '''
        Populates DataInstance object with empty parameters (string='' and float=0).
        '''
        g_code_1 = ''
        diameter_2 = 0
        flange_height_3 = 0
        radius_4 = 0
        fracture_forming_limit_5 = ''
        thickness_6 = 0
        hole_diameter_7 = 0
        limit_forming_ratio_8 = ''
        flange_height_9 = ''
        average_thickness_10 = ''
        bending_ratio_11 = ''
        toolpath_code_12 = ''
        is_prepared_13 = ''
        feed_rate_14 = 0
        step_down_15 = 0
        global_fld_16 = ''
        fld_per_tool_17 = ''
        fld_for_successful_tests_18 = ''
        fld_for_fractured_tests_19 = ''
        flange_height_diagram_20 = ''
        average_thickness_diagram_21 = ''
        is_fractured_22 = ''
        flange_height_23 = 0
        strain_distribution_24 = ''
        hole_expansion_ratio_25 = 0
        non_dimensional_flange_height_26 = 0
        non_dimensional_average_thickness_27 = 0
        global_lfr_28 = 0
        lfr_per_tool_29 = 0

        self.analysis_results = AnalysisResults()
        self.nc_program = NcProgram(g_code_1)
        self.part_model = PartModel(diameter_2, flange_height_3)
        self.forming_tool_model = FormingToolModel(radius_4)
        self.material_properties = MaterialProperties(fracture_forming_limit_5)
        self.blank_model = BlankModel(thickness_6, hole_diameter_7)
        self.conclusions = Conclusions(limit_forming_ratio_8, flange_height_9, average_thickness_10, bending_ratio_11)
        self.tool_path = ToolPath(toolpath_code_12)
        self.specimen = Specimen(is_prepared_13)
        self.forming_conditions = FormingConditions(feed_rate_14, step_down_15)
        self.fld = Fld(global_fld_16, fld_per_tool_17, fld_for_successful_tests_18, fld_for_fractured_tests_19)
        self.technological_parameters = TechnologicalParameters(flange_height_diagram_20, average_thickness_diagram_21)
        self.test_results = TestResults(is_fractured_22, flange_height_23, strain_distribution_24, hole_expansion_ratio_25, non_dimensional_flange_height_26, non_dimensional_average_thickness_27)
        self.lfr = Lfr(global_lfr_28, lfr_per_tool_29)

        self.save()

    def load(self):
        '''
        Creates a Instance object with data from a `data.ini` file.
        '''
        config = configparser.ConfigParser()
        config.read(self.datafile)
        g_code_1 = config.get('NC Program', 'g-code')
        diameter_2 = float(config.get('Part Model', 'diameter'))
        flange_height_3 = float(config.get('Part Model', 'flange height'))
        radius_4 = float(config.get('Forming Tool Model', 'radius'))
        fracture_forming_limit_5 = config.get('Material Properties', 'fracture forming limit')
        thickness_6 = float(config.get('Blank Model', 'thickness'))
        hole_diameter_7 = float(config.get('Blank Model', 'hole diameter'))
        limit_forming_ratio_8 = config.get('Conclusions', 'limit forming ratio')
        flange_height_9 = config.get('Conclusions', 'flange height')
        average_thickness_10 = config.get('Conclusions', 'average thickness')
        bending_ratio_11 = config.get('Conclusions', 'bending ratio')
        toolpath_code_12 = config.get('Tool Path', 'toolpath code')
        is_prepared_13 = config.get('Specimen', 'is prepared')
        feed_rate_14 = float(config.get('Forming Conditions', 'feed rate'))
        step_down_15 = float(config.get('Forming Conditions', 'step down'))
        global_fld_16 = config.get('FLD', 'global fld')
        fld_per_tool_17 = config.get('FLD', 'fld per tool')
        fld_for_successful_tests_18 = config.get('FLD', 'fld for successful tests')
        fld_for_fractured_tests_19 = config.get('FLD', 'fld for fractured tests')
        flange_height_diagram_20 = config.get('Technological Parameters', 'flange height diagram')
        average_thickness_diagram_21 = config.get('Technological Parameters', 'average thickness diagram')
        is_fractured_22 = config.get('Test Results', 'is fractured')
        flange_height_23 = float(config.get('Test Results', 'flange height'))
        strain_distribution_24 = config.get('Test Results', 'strain distribution')
        hole_expansion_ratio_25 = float(config.get('Test Results', 'hole expansion ratio'))
        non_dimensional_flange_height_26 = float(config.get('Test Results', 'non-dimensional flange height'))
        non_dimensional_average_thickness_27 = float(config.get('Test Results', 'non-dimensional average thickness'))
        global_lfr_28 = float(config.get('LFR', 'global lfr'))
        lfr_per_tool_29 = float(config.get('LFR', 'lfr per tool'))

        self.analysis_results = AnalysisResults()
        self.nc_program = NcProgram(g_code_1)
        self.part_model = PartModel(diameter_2, flange_height_3)
        self.forming_tool_model = FormingToolModel(radius_4)
        self.material_properties = MaterialProperties(fracture_forming_limit_5)
        self.blank_model = BlankModel(thickness_6, hole_diameter_7)
        self.conclusions = Conclusions(limit_forming_ratio_8, flange_height_9, average_thickness_10, bending_ratio_11)
        self.tool_path = ToolPath(toolpath_code_12)
        self.specimen = Specimen(is_prepared_13)
        self.forming_conditions = FormingConditions(feed_rate_14, step_down_15)
        self.fld = Fld(global_fld_16, fld_per_tool_17, fld_for_successful_tests_18, fld_for_fractured_tests_19)
        self.technological_parameters = TechnologicalParameters(flange_height_diagram_20, average_thickness_diagram_21)
        self.test_results = TestResults(is_fractured_22, flange_height_23, strain_distribution_24, hole_expansion_ratio_25, non_dimensional_flange_height_26, non_dimensional_average_thickness_27)
        self.lfr = Lfr(global_lfr_28, lfr_per_tool_29)


    def save(self):
        '''
        Make a backup copy of `data.ini` before saving the data.
        '''
        if not os.path.isfile(self.datafile):
            os.makedirs(self.datafile.replace('data.ini', ''))
            open(self.datafile, 'a').close()
        else:
            # Backup of 'data.ini'
            date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            datafile_backup = 'Data_Layer/%s/data_%s.ini' % (self.instance_name, date)
            shutil.copyfile(self.datafile, datafile_backup)

        config = configparser.ConfigParser()
        config['Analysis Results'] = {
        }
        config['NC Program'] = {
            'g-code': self.nc_program.g_code,
        }
        config['Part Model'] = {
            'diameter': self.part_model.diameter,
            'flange height': self.part_model.flange_height,
        }
        config['Forming Tool Model'] = {
            'radius': self.forming_tool_model.radius,
        }
        config['Material Properties'] = {
            'fracture forming limit': self.material_properties.fracture_forming_limit,
        }
        config['Blank Model'] = {
            'thickness': self.blank_model.thickness,
            'hole diameter': self.blank_model.hole_diameter,
        }
        config['Conclusions'] = {
            'limit forming ratio': self.conclusions.limit_forming_ratio,
            'flange height': self.conclusions.flange_height,
            'average thickness': self.conclusions.average_thickness,
            'bending ratio': self.conclusions.bending_ratio,
        }
        config['Tool Path'] = {
            'toolpath code': self.tool_path.toolpath_code,
        }
        config['Specimen'] = {
            'is prepared': self.specimen.is_prepared,
        }
        config['Forming Conditions'] = {
            'feed rate': self.forming_conditions.feed_rate,
            'step down': self.forming_conditions.step_down,
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
        config['Test Results'] = {
            'is fractured': self.test_results.is_fractured,
            'flange height': self.test_results.flange_height,
            'strain distribution': self.test_results.strain_distribution,
            'hole expansion ratio': self.test_results.hole_expansion_ratio,
            'non-dimensional flange height': self.test_results.non_dimensional_flange_height,
            'non-dimensional average thickness': self.test_results.non_dimensional_average_thickness,
        }
        config['LFR'] = {
            'global lfr': self.lfr.global_lfr,
            'lfr per tool': self.lfr.lfr_per_tool,
        }

        with open(self.datafile, 'w') as configfile:
            config.write(configfile)
    
