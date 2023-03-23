#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>
"""

def check_for_fracture(gcode):
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

if __name__ == '__main__':
    gcode = '%0001\nN0010 G54\nN0020 T0101 S1000 M03\nN0030 ...'
    is_fractured = check_for_fracture(gcode)
    print("Returned is_fractured = '%s'" % is_fractured)
