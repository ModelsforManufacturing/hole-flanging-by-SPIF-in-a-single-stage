#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>

read CSV and return a dictionary
"""

import csv          # CSV File Reading and Writing

def read_semantic_model(semantic_model_file):
    ''' Read a CSV file and return a list of dictionaries '''
    data = []
    with open(semantic_model_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def get_semantic_data(semantic_data, data_object, parameter):
    for row in semantic_data:
        if (row['Object name'] == data_object) and (row['Parameter name'] == parameter):
            return (row['Type'], row['Description'])
    print("Warning: Parameter's type not found!")

   

if __name__ == '__main__':
    pass

