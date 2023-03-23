#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>
"""

def measure_strain_distribution(instance_name):
    strain = ''
    print('Use ARGUS to obtain the strain distribution along the flange.')
    print('Save the results as a text file "strain.csv" and upload it to "Data_Layer/%s".' % instance_name)
    q = input('Is the file already uploaded? (Yes/No) ')
    q = q.lower()
    if q in ['yes', 'y']:
        strain = 'strain.csv'
    return strain

if __name__ == '__main__':
    instance_name = 'prueba'
    strain = measure_strain_distribution(instance_name)
    print("Returned strain = '%s'" % strain)
