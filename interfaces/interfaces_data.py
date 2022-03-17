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
        hole_diameter_1 = float(parser.get('Blank Sheet', 'hole diameter'))
        thickness_2 = float(parser.get('Raw Material', 'thickness'))
        diameter_3 = float(parser.get('Design Part', 'diameter'))
        height_4 = float(parser.get('Design Part', 'height'))
        part_3d_5 = parser.get('Design Part', 'part 3d')
        radius_6 = float(parser.get('Forming Tool', 'radius'))
        elasticity_modulus_7 = float(parser.get('Elastic Behaviour', 'elasticity modulus'))
        poisson_ratio_8 = float(parser.get('Elastic Behaviour', 'poisson ratio'))
        strain_stress_curve_9 = parser.get('Plastic Behaviour', 'strain-stress curve')
        anisotropy_coefficients_10 = parser.get('Plastic Behaviour', 'anisotropy coefficients')
        fracture_curve_11 = parser.get('Fracture Behaviour', 'fracture curve')
        step_down_12 = float(parser.get('Strategy', 'step down'))
        feedrate_13 = float(parser.get('Strategy', 'feedrate'))
        apt_code_14 = parser.get('NC Program', 'apt code')
        process_3d_15 = parser.get('NC Model', 'process 3d')
        toolpath_code_16 = parser.get('Tool Trajectory', 'toolpath code')
        analysis_model_17 = parser.get('Simulation Model', 'analysis model')
        analysis_output_18 = parser.get('Simulation Results', 'analysis output')
        strain_distribution_19 = parser.get('Simulated Part', 'strain distribution')
        fracture_location_20 = parser.get('Simulated Part', 'fracture location')
        flange_height_21 = float(parser.get('Simulation Issues', 'flange height'))
        failed_22 = parser.get('Manufactured Part', 'failed')
        fracture_location_23 = parser.get('Manufactured Part', 'fracture location')
        height_24 = float(parser.get('Manufactured Part', 'height'))
        diameter_25 = float(parser.get('Manufactured Part', 'diameter'))
        photos_26 = parser.get('Manufactured Part', 'photos')
        strain_distribution_27 = parser.get('Analyzed Part', 'strain distribution')
        thickness_profile_28 = parser.get('Analyzed Part', 'thickness profile')
        fractographies_29 = parser.get('Analyzed Part', 'fractographies')
        flange_height_30 = float(parser.get('Manufacturing Issues', 'flange height'))


        self.blank_sheet = BlankSheet(hole_diameter_1)
        self.raw_material = RawMaterial(thickness_2)
        self.design_part = DesignPart(diameter_3, height_4, part_3d_5)
        self.forming_tool = FormingTool(radius_6)
        self.elastic_behaviour = ElasticBehaviour(elasticity_modulus_7, poisson_ratio_8)
        self.plastic_behaviour = PlasticBehaviour(strain_stress_curve_9, anisotropy_coefficients_10)
        self.fracture_behaviour = FractureBehaviour(fracture_curve_11)
        self.strategy = Strategy(step_down_12, feedrate_13)
        self.nc_program = NcProgram(apt_code_14)
        self.nc_model = NcModel(process_3d_15)
        self.tool_trajectory = ToolTrajectory(toolpath_code_16)
        self.simulation_model = SimulationModel(analysis_model_17)
        self.simulation_results = SimulationResults(analysis_output_18)
        self.simulated_part = SimulatedPart(strain_distribution_19, fracture_location_20)
        self.simulation_issues = SimulationIssues(flange_height_21)
        self.manufactured_part = ManufacturedPart(failed_22, fracture_location_23, height_24, diameter_25, photos_26)
        self.analyzed_part = AnalyzedPart(strain_distribution_27, thickness_profile_28, fractographies_29)
        self.manufacturing_issues = ManufacturingIssues(flange_height_30)


    def save(self):
        '''
        Make a backup copy of `data.ini` before saving the data.
        '''
        # Backup of 'data.ini'
        date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        datafile_backup = 'Data_Layer/%s/data_%s.ini' % (self.instance_name, date)
        shutil.copyfile(self.datafile, datafile_backup)

        config = configparser.ConfigParser()
        config['Blank Sheet'] = {
            'hole diameter': self.blank_sheet.hole_diameter,
        }
        config['Raw Material'] = {
            'thickness': self.raw_material.thickness,
        }
        config['Design Part'] = {
            'diameter': self.design_part.diameter,
            'height': self.design_part.height,
            'part 3d': self.design_part.part_3d,
        }
        config['Forming Tool'] = {
            'radius': self.forming_tool.radius,
        }
        config['Elastic Behaviour'] = {
            'elasticity modulus': self.elastic_behaviour.elasticity_modulus,
            'poisson ratio': self.elastic_behaviour.poisson_ratio,
        }
        config['Plastic Behaviour'] = {
            'strain-stress curve': self.plastic_behaviour.strain_stress_curve,
            'anisotropy coefficients': self.plastic_behaviour.anisotropy_coefficients,
        }
        config['Fracture Behaviour'] = {
            'fracture curve': self.fracture_behaviour.fracture_curve,
        }
        config['Strategy'] = {
            'step down': self.strategy.step_down,
            'feedrate': self.strategy.feedrate,
        }
        config['NC Program'] = {
            'apt code': self.nc_program.apt_code,
        }
        config['NC Model'] = {
            'process 3d': self.nc_model.process_3d,
        }
        config['Tool Trajectory'] = {
            'toolpath code': self.tool_trajectory.toolpath_code,
        }
        config['Simulation Model'] = {
            'analysis model': self.simulation_model.analysis_model,
        }
        config['Simulation Results'] = {
            'analysis output': self.simulation_results.analysis_output,
        }
        config['Simulated Part'] = {
            'strain distribution': self.simulated_part.strain_distribution,
            'fracture location': self.simulated_part.fracture_location,
        }
        config['Simulation Issues'] = {
            'flange height': self.simulation_issues.flange_height,
        }
        config['Manufactured Part'] = {
            'failed': self.manufactured_part.failed,
            'fracture location': self.manufactured_part.fracture_location,
            'height': self.manufactured_part.height,
            'diameter': self.manufactured_part.diameter,
            'photos': self.manufactured_part.photos,
        }
        config['Analyzed Part'] = {
            'strain distribution': self.analyzed_part.strain_distribution,
            'thickness profile': self.analyzed_part.thickness_profile,
            'fractographies': self.analyzed_part.fractographies,
        }
        config['Manufacturing Issues'] = {
            'flange height': self.manufacturing_issues.flange_height,
        }

        
        with open(self.datafile, 'w') as configfile:
            config.write(configfile)
    
