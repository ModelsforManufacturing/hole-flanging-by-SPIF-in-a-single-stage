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

class FlangeabilityResults:
    def __init__(self, ):
        pass
    def load(self, instance_name):
        i = DataInstance(instance_name)
        i.load()

    def save(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        i.save()

class FlangeabilityParameters:
    def __init__(self, overall_lfr, lfr_per_tool):
        self.overall_lfr = overall_lfr
        self.lfr_per_tool = lfr_per_tool

    def load(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        self.overall_lfr = i.flangeability_parameters.overall_lfr
        self.lfr_per_tool = i.flangeability_parameters.lfr_per_tool

    def save(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        i.flangeability_parameters.overall_lfr = self.overall_lfr
        i.flangeability_parameters.lfr_per_tool = self.lfr_per_tool
        i.save()

class Fld:
    def __init__(self, overall_fld, fld_per_tool, fld_for_successful_tests, fld_for_fractured_tests):
        self.overall_fld = overall_fld
        self.fld_per_tool = fld_per_tool
        self.fld_for_successful_tests = fld_for_successful_tests
        self.fld_for_fractured_tests = fld_for_fractured_tests

    def load(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        self.overall_fld = i.fld.overall_fld
        self.fld_per_tool = i.fld.fld_per_tool
        self.fld_for_successful_tests = i.fld.fld_for_successful_tests
        self.fld_for_fractured_tests = i.fld.fld_for_fractured_tests

    def save(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        i.fld.overall_fld = self.overall_fld
        i.fld.fld_per_tool = self.fld_per_tool
        i.fld.fld_for_successful_tests = self.fld_for_successful_tests
        i.fld.fld_for_fractured_tests = self.fld_for_fractured_tests
        i.save()

class FlangeabilityDiagrams:
    def __init__(self, flange_height_diagram, average_thickness_diagram):
        self.flange_height_diagram = flange_height_diagram
        self.average_thickness_diagram = average_thickness_diagram

    def load(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        self.flange_height_diagram = i.flangeability_diagrams.flange_height_diagram
        self.average_thickness_diagram = i.flangeability_diagrams.average_thickness_diagram

    def save(self, instance_name):
        i = DataInstance(instance_name)
        i.load()
        i.flangeability_diagrams.flange_height_diagram = self.flange_height_diagram
        i.flangeability_diagrams.average_thickness_diagram = self.average_thickness_diagram
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
        thickness_1 = 0
        hole_diameter_2 = 0
        diameter_3 = 0
        flange_height_4 = 0
        toolpath_code_5 = ''
        feed_rate_6 = 0
        step_down_7 = 0
        g_code_8 = ''
        is_prepared_9 = ''
        fracture_forming_limit_10 = ''
        is_fractured_11 = ''
        flange_height_12 = 0
        strain_distribution_13 = ''
        hole_expansion_ratio_14 = 0
        non_dimensional_flange_height_15 = 0
        non_dimensional_average_thickness_16 = 0
        overall_lfr_17 = 0
        lfr_per_tool_18 = 0
        overall_fld_19 = ''
        fld_per_tool_20 = ''
        fld_for_successful_tests_21 = ''
        fld_for_fractured_tests_22 = ''
        flange_height_diagram_23 = ''
        average_thickness_diagram_24 = ''
        radius_25 = 0

        self.blank_model = BlankModel(thickness_1, hole_diameter_2)
        self.part_model = PartModel(diameter_3, flange_height_4)
        self.tool_path = ToolPath(toolpath_code_5)
        self.forming_conditions = FormingConditions(feed_rate_6, step_down_7)
        self.nc_program = NcProgram(g_code_8)
        self.specimen = Specimen(is_prepared_9)
        self.material_properties = MaterialProperties(fracture_forming_limit_10)
        self.test_results = TestResults(is_fractured_11, flange_height_12, strain_distribution_13, hole_expansion_ratio_14, non_dimensional_flange_height_15, non_dimensional_average_thickness_16)
        self.flangeability_results = FlangeabilityResults()
        self.flangeability_parameters = FlangeabilityParameters(overall_lfr_17, lfr_per_tool_18)
        self.fld = Fld(overall_fld_19, fld_per_tool_20, fld_for_successful_tests_21, fld_for_fractured_tests_22)
        self.flangeability_diagrams = FlangeabilityDiagrams(flange_height_diagram_23, average_thickness_diagram_24)
        self.forming_tool_model = FormingToolModel(radius_25)

        self.save()

    def load(self):
        '''
        Creates a Instance object with data from a `data.ini` file.
        '''
        config = configparser.ConfigParser()
        config.read(self.datafile)
        thickness_1 = float(config.get('Blank Model', 'thickness'))
        hole_diameter_2 = float(config.get('Blank Model', 'hole diameter'))
        diameter_3 = float(config.get('Part Model', 'diameter'))
        flange_height_4 = float(config.get('Part Model', 'flange height'))
        toolpath_code_5 = config.get('Tool Path', 'toolpath code')
        feed_rate_6 = float(config.get('Forming Conditions', 'feed rate'))
        step_down_7 = float(config.get('Forming Conditions', 'step down'))
        g_code_8 = config.get('NC Program', 'g-code')
        is_prepared_9 = config.get('Specimen', 'is prepared')
        fracture_forming_limit_10 = config.get('Material Properties', 'fracture forming limit')
        is_fractured_11 = config.get('Test Results', 'is fractured')
        flange_height_12 = float(config.get('Test Results', 'flange height'))
        strain_distribution_13 = config.get('Test Results', 'strain distribution')
        hole_expansion_ratio_14 = float(config.get('Test Results', 'hole expansion ratio'))
        non_dimensional_flange_height_15 = float(config.get('Test Results', 'non-dimensional flange height'))
        non_dimensional_average_thickness_16 = float(config.get('Test Results', 'non-dimensional average thickness'))
        overall_lfr_17 = float(config.get('Flangeability Parameters', 'overall lfr'))
        lfr_per_tool_18 = float(config.get('Flangeability Parameters', 'lfr per tool'))
        overall_fld_19 = config.get('FLD', 'overall fld')
        fld_per_tool_20 = config.get('FLD', 'fld per tool')
        fld_for_successful_tests_21 = config.get('FLD', 'fld for successful tests')
        fld_for_fractured_tests_22 = config.get('FLD', 'fld for fractured tests')
        flange_height_diagram_23 = config.get('Flangeability Diagrams', 'flange height diagram')
        average_thickness_diagram_24 = config.get('Flangeability Diagrams', 'average thickness diagram')
        radius_25 = float(config.get('Forming Tool Model', 'radius'))

        self.blank_model = BlankModel(thickness_1, hole_diameter_2)
        self.part_model = PartModel(diameter_3, flange_height_4)
        self.tool_path = ToolPath(toolpath_code_5)
        self.forming_conditions = FormingConditions(feed_rate_6, step_down_7)
        self.nc_program = NcProgram(g_code_8)
        self.specimen = Specimen(is_prepared_9)
        self.material_properties = MaterialProperties(fracture_forming_limit_10)
        self.test_results = TestResults(is_fractured_11, flange_height_12, strain_distribution_13, hole_expansion_ratio_14, non_dimensional_flange_height_15, non_dimensional_average_thickness_16)
        self.flangeability_results = FlangeabilityResults()
        self.flangeability_parameters = FlangeabilityParameters(overall_lfr_17, lfr_per_tool_18)
        self.fld = Fld(overall_fld_19, fld_per_tool_20, fld_for_successful_tests_21, fld_for_fractured_tests_22)
        self.flangeability_diagrams = FlangeabilityDiagrams(flange_height_diagram_23, average_thickness_diagram_24)
        self.forming_tool_model = FormingToolModel(radius_25)


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
        config['Blank Model'] = {
            'thickness': self.blank_model.thickness,
            'hole diameter': self.blank_model.hole_diameter,
        }
        config['Part Model'] = {
            'diameter': self.part_model.diameter,
            'flange height': self.part_model.flange_height,
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
        config['Material Properties'] = {
            'fracture forming limit': self.material_properties.fracture_forming_limit,
        }
        config['Test Results'] = {
            'is fractured': self.test_results.is_fractured,
            'flange height': self.test_results.flange_height,
            'strain distribution': self.test_results.strain_distribution,
            'hole expansion ratio': self.test_results.hole_expansion_ratio,
            'non-dimensional flange height': self.test_results.non_dimensional_flange_height,
            'non-dimensional average thickness': self.test_results.non_dimensional_average_thickness,
        }
        config['Flangeability Results'] = {
        }
        config['Flangeability Parameters'] = {
            'overall lfr': self.flangeability_parameters.overall_lfr,
            'lfr per tool': self.flangeability_parameters.lfr_per_tool,
        }
        config['FLD'] = {
            'overall fld': self.fld.overall_fld,
            'fld per tool': self.fld.fld_per_tool,
            'fld for successful tests': self.fld.fld_for_successful_tests,
            'fld for fractured tests': self.fld.fld_for_fractured_tests,
        }
        config['Flangeability Diagrams'] = {
            'flange height diagram': self.flangeability_diagrams.flange_height_diagram,
            'average thickness diagram': self.flangeability_diagrams.average_thickness_diagram,
        }
        config['Forming Tool Model'] = {
            'radius': self.forming_tool_model.radius,
        }

        with open(self.datafile, 'w') as configfile:
            config.write(configfile)
    
