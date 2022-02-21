#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>

"""

import data.interfaces as data
import service.interfaces as service


"""
Retrieve data from the Data Layer.
"""
datafile = 'example_01.ini'
variables = data.retrieve_data(datafile)
blank_d, blank_t, part_d, part_h, part_tol, part_3d, tool_r = variables


"""
Execute a task defined in Service Layer.

Activity: A11 Update Design Part
Task: T1 Calculate flange height
Rule: R1 Update the flange height according to an equation
"""
part_h = service.calculate_flange_height(blank_d, part_d, simul_issues_h)


"""
Save data to the Data Layer.
Save all data to another file and trace life cycle of files.
File name format: <instance_name>_A<activity_number>_T<task_number>.ini
"""
datafile = 'example_01_A11_T1.ini'
variables = (blank_d, blank_t, part_d, part_h, part_tol, part_3d, tool_r)
data.save_data(variables, datafile)



