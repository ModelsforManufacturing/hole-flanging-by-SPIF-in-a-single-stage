#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Domingo Morales Palma <dmpalma@us.es>

Interfaces for the definition of Objects and Parameters of the Data Model.
Implementation must be done in module:
    Data_Layer.data_interface_implementation

This file has been generated automatically.
'''

class AnalysisResultsInterface:
    '''
    This interface must be implemented by class:
        BlankModel
    in module:
        Data_Layer.data_interface_implementation

    Description: TODO
    '''
    def __init__(self, ):
        '''
        Use the object constructor to retrieve these parameters:

        '''
        pass

    def save(self):
        ''' Save parameter values. '''
        pass

class NcProgramInterface:
    '''
    This interface must be implemented by class:
        BlankModel
    in module:
        Data_Layer.data_interface_implementation

    Description: TODO
    '''
    def __init__(self, g_code):
        '''
        Use the object constructor to retrieve these parameters:
        g_code -- (str) 

        '''
        pass

    def save(self):
        ''' Save parameter values. '''
        pass

class PartModelInterface:
    '''
    This interface must be implemented by class:
        BlankModel
    in module:
        Data_Layer.data_interface_implementation

    Description: TODO
    '''
    def __init__(self, diameter, flange_height):
        '''
        Use the object constructor to retrieve these parameters:
        diameter -- (float) Units: mm. Inner diameter of the hole-flanged part to be manufactured.
        flange_height -- (float) Units: mm. Theoretical flange height measured from the external flat surface.

        '''
        pass

    def save(self):
        ''' Save parameter values. '''
        pass

class FormingToolModelInterface:
    '''
    This interface must be implemented by class:
        BlankModel
    in module:
        Data_Layer.data_interface_implementation

    Description: TODO
    '''
    def __init__(self, radius):
        '''
        Use the object constructor to retrieve these parameters:
        radius -- (float) Units: mm. Forming tool radius.

        '''
        pass

    def save(self):
        ''' Save parameter values. '''
        pass

class MaterialPropertiesInterface:
    '''
    This interface must be implemented by class:
        BlankModel
    in module:
        Data_Layer.data_interface_implementation

    Description: TODO
    '''
    def __init__(self, fracture_forming_limit):
        '''
        Use the object constructor to retrieve these parameters:
        fracture_forming_limit -- (str) Table with pairs of major and minor strain values

        '''
        pass

    def save(self):
        ''' Save parameter values. '''
        pass

class BlankModelInterface:
    '''
    This interface must be implemented by class:
        BlankModel
    in module:
        Data_Layer.data_interface_implementation

    Description: TODO
    '''
    def __init__(self, thickness, hole_diameter):
        '''
        Use the object constructor to retrieve these parameters:
        thickness -- (float) Units: mm. Initial sheet thickness.
        hole_diameter -- (float) Units: mm. Diameter of the hole to be cut to the blank sheet.

        '''
        pass

    def save(self):
        ''' Save parameter values. '''
        pass

class ConclusionsInterface:
    '''
    This interface must be implemented by class:
        BlankModel
    in module:
        Data_Layer.data_interface_implementation

    Description: TODO
    '''
    def __init__(self, limit_forming_ratio, flange_height, average_thickness, bending_ratio):
        '''
        Use the object constructor to retrieve these parameters:
        limit_forming_ratio -- (str) 
        flange_height -- (str) 
        average_thickness -- (str) 
        bending_ratio -- (str) 

        '''
        pass

    def save(self):
        ''' Save parameter values. '''
        pass

class ToolPathInterface:
    '''
    This interface must be implemented by class:
        BlankModel
    in module:
        Data_Layer.data_interface_implementation

    Description: TODO
    '''
    def __init__(self, toolpath_code):
        '''
        Use the object constructor to retrieve these parameters:
        toolpath_code -- (str) It can be APT, G-code, etc. It must contain the tool path coordinates, tool feed rate and step down.

        '''
        pass

    def save(self):
        ''' Save parameter values. '''
        pass

class SpecimenInterface:
    '''
    This interface must be implemented by class:
        BlankModel
    in module:
        Data_Layer.data_interface_implementation

    Description: TODO
    '''
    def __init__(self, is_prepared):
        '''
        Use the object constructor to retrieve these parameters:
        is_prepared -- (str) 

        '''
        pass

    def save(self):
        ''' Save parameter values. '''
        pass

class FormingConditionsInterface:
    '''
    This interface must be implemented by class:
        BlankModel
    in module:
        Data_Layer.data_interface_implementation

    Description: TODO
    '''
    def __init__(self, feed_rate, step_down):
        '''
        Use the object constructor to retrieve these parameters:
        feed_rate -- (float) Units: mm/min. Feed rate of the forming tool.
        step_down -- (float) Units: mm. Step down of the forming tool following an helical tool path.

        '''
        pass

    def save(self):
        ''' Save parameter values. '''
        pass

class FldInterface:
    '''
    This interface must be implemented by class:
        BlankModel
    in module:
        Data_Layer.data_interface_implementation

    Description: TODO
    '''
    def __init__(self, global_fld, fld_per_tool, fld_for_successful_tests, fld_for_fractured_tests):
        '''
        Use the object constructor to retrieve these parameters:
        global_fld -- (str) Name of image file. FLD includes FFL curve and strain distribution for all tests.
        fld_per_tool -- (str) 
        fld_for_successful_tests -- (str) 
        fld_for_fractured_tests -- (str) 

        '''
        pass

    def save(self):
        ''' Save parameter values. '''
        pass

class TechnologicalParametersInterface:
    '''
    This interface must be implemented by class:
        BlankModel
    in module:
        Data_Layer.data_interface_implementation

    Description: TODO
    '''
    def __init__(self, flange_height_diagram, average_thickness_diagram):
        '''
        Use the object constructor to retrieve these parameters:
        flange_height_diagram -- (str) 
        average_thickness_diagram -- (str) 

        '''
        pass

    def save(self):
        ''' Save parameter values. '''
        pass

class TestResultsInterface:
    '''
    This interface must be implemented by class:
        BlankModel
    in module:
        Data_Layer.data_interface_implementation

    Description: TODO
    '''
    def __init__(self, is_fractured, flange_height, strain_distribution, hole_expansion_ratio, non_dimensional_flange_height, non_dimensional_average_thickness):
        '''
        Use the object constructor to retrieve these parameters:
        is_fractured -- (str) 
        flange_height -- (float) Units: mm. Flange height of the produced part measured from the external flat surface.
        strain_distribution -- (str) 
        hole_expansion_ratio -- (float) Units: non-dimensional. Initial to final diameter ratio, d0/df.
        non_dimensional_flange_height -- (float) Units: non-dimensional. Flange height to final diameter ratio, h/df.
        non_dimensional_average_thickness -- (float) Units: non-dimensional. Average thickness along the flange to initial thickness ratio, t/t0.

        '''
        pass

    def save(self):
        ''' Save parameter values. '''
        pass

class LfrInterface:
    '''
    This interface must be implemented by class:
        BlankModel
    in module:
        Data_Layer.data_interface_implementation

    Description: TODO
    '''
    def __init__(self, global_lfr, lfr_per_tool):
        '''
        Use the object constructor to retrieve these parameters:
        global_lfr -- (float) Units: non-dimensional. Limit forming ratio from all experimental tests.
        lfr_per_tool -- (float) Units: non-dimensional. Limit forming ratio from experimental tests using the same forming tool.

        '''
        pass

    def save(self):
        ''' Save parameter values. '''
        pass


