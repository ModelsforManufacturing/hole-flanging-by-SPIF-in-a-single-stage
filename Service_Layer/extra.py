#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>

Temporary working module.

"""

import os
import configparser # Configuration file parser
import shutil       # High-level file operations
import datetime     # Basic date and time types



############################################################################

# Copied from interfaces/data_classes.py and interfaces/interfaces_data.py

class BlankModel:
    ''' Description: TODO '''
    def __init__(self, thickness, hole_diameter):
        '''
        Keyword arguments:
        thickness -- (float) Units: mm. Initial sheet thickness.
        hole_diameter -- (float) Units: mm. Diameter of the hole to be cut to the blank sheet.

        '''
        self.thickness = thickness
        self.hole_diameter = hole_diameter


class PartModel:
    ''' Description: TODO '''
    def __init__(self, diameter, flange_height):
        '''
        Keyword arguments:
        diameter -- (float) Units: mm. Inner diameter of the hole-flanged part to be manufactured.
        flange_height -- (float) Units: mm. Theoretical flange height measured from the external flat surface.

        '''
        self.diameter = diameter
        self.flange_height = flange_height


class FormingToolModel:
    ''' Description: TODO '''
    def __init__(self, radius):
        '''
        Keyword arguments:
        radius -- (float) Units: mm. Forming tool radius.

        '''
        self.radius = radius


class ToolPath:
    ''' Description: TODO '''
    def __init__(self, toolpath_code):
        '''
        Keyword arguments:
        toolpath_code -- (string) It can be APT, G-code, etc. It must contain the tool path coordinates, tool feed rate and step down.

        '''
        self.toolpath_code = toolpath_code


class FormingConditions:
    ''' Description: TODO '''
    def __init__(self, feed_rate, step_down):
        '''
        Keyword arguments:
        feed_rate -- (float) Units: mm/min. Feed rate of the forming tool.
        step_down -- (float) Units: mm. Step down of the forming tool following an helical tool path.

        '''
        self.feed_rate = feed_rate
        self.step_down = step_down


class NcProgram:
    ''' Description: TODO '''
    def __init__(self, g_code):
        '''
        Keyword arguments:
        g_code -- (string) 

        '''
        self.g_code = g_code


class Specimen:
    ''' Description: TODO '''
    def __init__(self, is_prepared):
        '''
        Keyword arguments:
        is_prepared -- (string) 

        '''
        self.is_prepared = is_prepared


class TestResults:
    ''' Description: TODO '''
    def __init__(self, is_fractured, flange_height, strain_distribution, hole_expansion_ratio, non_dimensional_flange_height, non_dimensional_average_thickness):
        '''
        Keyword arguments:
        is_fractured -- (string) 
        flange_height -- (float) Units: mm. Flange height of the produced part measured from the external flat surface.
        strain_distribution -- (string) 
        hole_expansion_ratio -- (float) Units: non-dimensional. Initial to final diameter ratio, d0/df.
        non_dimensional_flange_height -- (float) Units: non-dimensional. Flange height to final diameter ratio, h/df.
        non_dimensional_average_thickness -- (float) Units: non-dimensional. Average thickness along the flange to initial thickness ratio, t/t0.

        '''
        self.is_fractured = is_fractured
        self.flange_height = flange_height
        self.strain_distribution = strain_distribution
        self.hole_expansion_ratio = hole_expansion_ratio
        self.non_dimensional_flange_height = non_dimensional_flange_height
        self.non_dimensional_average_thickness = non_dimensional_average_thickness


class MaterialProperties:
    ''' Description: TODO '''
    def __init__(self, fracture_forming_limit):
        '''
        Keyword arguments:
        fracture_forming_limit -- (string) Table with pairs of major and minor strain values

        '''
        self.fracture_forming_limit = fracture_forming_limit


class AnalysisResults:
    ''' Description: TODO '''
    def __init__(self, ):
        '''
        Keyword arguments:

        '''


class Lfr:
    ''' Description: TODO '''
    def __init__(self, global_lfr, lfr_per_tool):
        '''
        Keyword arguments:
        global_lfr -- (float) Units: non-dimensional. Limit forming ratio from all experimental tests.
        lfr_per_tool -- (float) Units: non-dimensional. Limit forming ratio from experimental tests using the same forming tool.

        '''
        self.global_lfr = global_lfr
        self.lfr_per_tool = lfr_per_tool


class Fld:
    ''' Description: TODO '''
    def __init__(self, global_fld, fld_per_tool, fld_for_successful_tests, fld_for_fractured_tests):
        '''
        Keyword arguments:
        global_fld -- (string) Name of image file. FLD includes FFL curve and strain distribution for all tests.
        fld_per_tool -- (string) 
        fld_for_successful_tests -- (string) 
        fld_for_fractured_tests -- (string) 

        '''
        self.global_fld = global_fld
        self.fld_per_tool = fld_per_tool
        self.fld_for_successful_tests = fld_for_successful_tests
        self.fld_for_fractured_tests = fld_for_fractured_tests


class TechnologicalParameters:
    ''' Description: TODO '''
    def __init__(self, flange_height_diagram, average_thickness_diagram):
        '''
        Keyword arguments:
        flange_height_diagram -- (string) 
        average_thickness_diagram -- (string) 

        '''
        self.flange_height_diagram = flange_height_diagram
        self.average_thickness_diagram = average_thickness_diagram


class Conclusions:
    ''' Description: TODO '''
    def __init__(self, limit_forming_ratio, flange_height, average_thickness, bending_ratio):
        '''
        Keyword arguments:
        limit_forming_ratio -- (string) 
        flange_height -- (string) 
        average_thickness -- (string) 
        bending_ratio -- (string) 

        '''
        self.limit_forming_ratio = limit_forming_ratio
        self.flange_height = flange_height
        self.average_thickness = average_thickness
        self.bending_ratio = bending_ratio


class Instance:
    def __init__(self, instance_name):
        '''
        Creates a Instance object with data from a `data.ini` file.
        
        Keyword arguments:
        instance_name -- string
        '''
        self.instance_name = instance_name
        datafile = 'Data_Layer/%s/data.ini' % instance_name
        self.datafile = datafile
        
    def new(self, d0, R, t0=1.6, df=95.8, f=1000, sd=0.2):
        parser = configparser.ConfigParser()
        parser.read(self.datafile)
        thickness_1 = float(t0)
        hole_diameter_2 = d0
        diameter_3 = df
        flange_height_4 = 0
        radius_5 = R
        toolpath_code_6 = ''
        feed_rate_7 = f
        step_down_8 = sd
        g_code_9 = ''
        is_prepared_10 = ''
        is_fractured_11 = ''
        flange_height_12 = 0
        strain_distribution_13 = ''
        hole_expansion_ratio_14 = 0
        non_dimensional_flange_height_15 = 0
        non_dimensional_average_thickness_16 = 0
        fracture_forming_limit_17 = 'files/fracture_forming_limit.csv'
        global_lfr_18 = 0
        lfr_per_tool_19 = 0
        global_fld_20 = ''
        fld_per_tool_21 = ''
        fld_for_successful_tests_22 = ''
        fld_for_fractured_tests_23 = ''
        flange_height_diagram_24 = ''
        average_thickness_diagram_25 = ''
        limit_forming_ratio_26 = ''
        flange_height_27 = ''
        average_thickness_28 = ''
        bending_ratio_29 = ''

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


    def read(self):
        parser = configparser.ConfigParser()
        parser.read(self.datafile)
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
        instance_dir = 'Data_Layer/%s' % self.instance_name
        if os.path.exists(self.datafile):
            date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            datafile_backup = 'Data_Layer/%s/data_%s.ini' % (self.instance_name, date)
            shutil.copyfile(self.datafile, datafile_backup)
        if not os.path.exists(instance_dir):
            os.makedirs(instance_dir)

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
    
############################################################################

def new_instance(instance):
    i = Instance(instance)
    d0 = input('Enter pre-cut hole diameter of the specimen (mm): ')
    R = input('Enter tool radius (mm) [6, 8, 10]: ')
    i.new(d0, R)
    i.save()

def find_instances():
    data_layer = 'Data_Layer/'
    instances = []
    for root, dirs, files in os.walk(data_layer):
        for name in files:
            if name == 'data.ini':
                instance = root.split(data_layer)[1]
                instances.append(instance)
#    print(instances)
    return instances

def list_instances():
    instances = find_instances()
    for instance in instances:
        i = Instance(instance)
        i.read()
        t0 = i.blank_model.thickness
        d0 = i.blank_model.hole_diameter
        R = i.forming_tool_model.radius
        f = i.forming_conditions.feed_rate
        sd = i.forming_conditions.step_down
        print('%s: d0 = %.1f mm, R = %d mm' % (instance, d0, R))
         

def print_status(instance):
    print('****************************************')
    print('Status of instance "%s":' % instance)
    try:
        i = Instance(instance)
        i.read()
        t0 = i.blank_model.thickness
        d0 = i.blank_model.hole_diameter
        R = i.forming_tool_model.radius
        f = i.forming_conditions.feed_rate
        sd = i.forming_conditions.step_down
        h = i.part_model.flange_height
        toolpath = i.tool_path.toolpath_code
        g_code = i.nc_program.g_code
        if g_code == '':
            print('    G-code not found.')
            print('You must run Action 1.')
            return
        else:
            print('    t0 = %0.1f mm, d0 = %0.1f mm, R = %d mm, feedrate = %d mm/min, step-down = %0.1f mm' % (t0, d0, R, f, sd))
            print('    theoretical flange height, h = %0.1f mm' % h)
            print('    tool path in file "%s"' % toolpath)
            print('    G-code in file "%s"' % g_code)
            print('Action 1 completed.')

        is_prepared = i.specimen.is_prepared
        if not is_prepared in ['yes', 'y']:
            print('    The specimen has not been prepared yet.')
            print('You must run Action 2.')
            return
        else:
            print('    The specimen has been prepared.')
            print('Action 2 completed.')
        
        is_fractured = i.test_results.is_fractured
        if not is_fractured in ['yes', 'y', 'no', 'n']:
            print('    The experimental hole flanging test has not been performed yet.')
            print('You must run Action 3.')
            return
        else:
            print('    The experimental hole flanging test has been performed.')
            print('Action 3 completed.')

        if is_fractured in ['yes', 'y']:
            print('    The experimental test failed: a fracture was found.')
        else:
            print('    The experimental test was successful, no fracture was found.')

        fh = i.test_results.flange_height
        if is_fractured in ['no', 'n']:
            if not fh > 0:
                print('    The flange height has not been measured yet.')
                print('You must run Action 4.')
                return
            else:
                print('    Measured flange height = %.1f mm' % fh)
            print('Action 4 completed.')

        strain = i.test_results.strain_distribution
        if is_fractured in ['yes', 'y', 'no', 'n']:
            if strain == '':
                print('    The strain distribution has not been measured yet.')
                print('You must run Action 5.')
                return
            else:
                print('    Measured strain distribution in file "%s".' % strain)
            print('Action 5 completed.')

        her = i.test_results.hole_expansion_ratio
        h_df = i.test_results.non_dimensional_flange_height
        t_t0 = i.test_results.non_dimensional_average_thickness
        if is_fractured in ['no', 'n']:
            if not t_t0 > 0:
                print('    Variables not calculated yet: HER, h/df, t/t0.')
                print('You must run Action 6.')
                return
            else:
                print('    HER = %.2f, h/df = %.2f, t/t0 = %.2f.' % (her, h_df, t_t0))
            print('Action 6 completed.')

        global_lfr = i.lfr.global_lfr
        lfr_per_tool = i.lfr.lfr_per_tool
        if is_fractured in ['no', 'n']:
            if not lfr_per_tool > 0:
                print('    Variables not calculated yet: global LFR and LFR per tool radius %d.' % R)
                print('You must run Action 7.')
                return
            else:
                print('    Global LFR = %.2f, LFR using R%d = %.2f.' % (global_lfr, R, lfr_per_tool))
            print('Action 7 completed.')
        print('****************************************')
    except:
        print('Instance "%s" does not exist.' % instance)
        print('Use arguments "--instance %s --action 1" to create it.' % instance)

############################################################################






def calculate_global_lfr(her, is_fracture):
    instances = find_instances()
    her_list = []
    for instance in instances:
        i = Instance(instance)
        i.read()
        her = i.test_results.hole_expansion_ratio
        her_list.append(her)
    global_lfr = max(her_list)    

    return global_lfr

def calculate_lfr_per_tool(her, is_fracture, R):
    instances = find_instances()
    her_list = []
    for instance in instances:
        i = Instance(instance)
        i.read()
        tool_R = i.forming_tool_model.radius
        if tool_R == R:
            her = i.test_results.hole_expansion_ratio
            her_list.append(her)
    lfr_per_tool = max(her_list)    

    return lfr_per_tool

def plot_global_fld(instance, strain_distribution, fracture_forming_limit):
    import Service_Layer.plot_results.plot_FLD as plot
    global_fld = plot.plot_fld(instance, strain_distribution, fracture_forming_limit)
    return global_fld
    
def plot_fld_per_tool(strain_distribution, fracture_forming_limit, R):
    # TODO
    fld_per_tool = 'TBD'
    return fld_per_tool

def plot_fld_for_successful_tests(strain_distribution, fracture_forming_limit, is_fractured):
    # TODO
    fld_for_successful_tests = 'TBD'
    return fld_for_successful_tests

def plot_fld_for_fractured_tests(strain_distribution, fracture_forming_limit, is_fractured):
    # TODO
    fld_for_fractured_tests = 'TBD'
    return fld_for_fractured_tests

def plot_h_df(h_df):
    # TODO
    flange_height_diagram = 'TBD'
    return flange_height_diagram

def plot_t_t0(t_t0):
    # TODO
    average_thickness_diagram = 'TBD'
    return average_thickness_diagram

def conclusions_for_lfr(global_lfr, lfr_per_tool):
    # TODO
    print('LFR = %f' % global_lfr)
    print('LFR per tool = %f' % lfr_per_tool)
    conclusions_limit_forming_ratio = 'TBD'
    return conclusions_limit_forming_ratio
    
def conclusions_for_height(flange_height_diagram):
    # TODO
    conclusions_flange_height = 'TBD'
    return conclusions_flange_height
    
def conclusions_for_thickness(average_thickness_diagram):
    # TODO
    conclusions_average_thickness = 'TBD'
    return conclusions_average_thickness
    
def conclusions_for_t0_r(global_lfr, lfr_per_tool, global_fld, fld_per_tool, fld_for_successful_tests, fld_for_fractured_tests, flange_height_diagram, average_thickness_diagram):
    # TODO
    conclusions_bending_ratio = 'TBD'
    return conclusions_bending_ratio
    

if __name__ == '__main__':
    os.chdir('..')
    print_status('instance01')
