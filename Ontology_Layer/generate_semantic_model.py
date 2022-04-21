#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>

Read the definition of the enriched data model in GraphViz format and generate a CSV file with the list of objects and parameters and additional columns for the later definition of parameter's type and description.
"""

import pathlib      # Object-oriented filesystem paths
import csv          # CSV File Reading and Writing
import shutil       # High-level file operations
import datetime     # Basic date and time types
import parse_graphviz_data_model as pgv

def nodes2table(data_objects, field_names):
    ''' 
    Store graphviz nodes (objects and parameters) to a csv table.
    Return the csv table in a dictionary.
    
    First column: object name
    Second column: parameter name
    '''
    data = []
    for n in data_objects:
        data_object = data_objects[n]
        object_name = n

        if not 'parameter' in data_object:
            field = {f:'' for f in field_names}     # reset dictionary using csv field names
            field[field_names[0]] = object_name     # and add object name to the first column
            data.append(field)
            pass
        else:
            for param_name in data_object['parameter']:
                field = {f:'' for f in field_names} # reset dictionary using csv field names
                field[field_names[0]] = object_name # and add object name to the first column
                field[field_names[1]] = param_name  # parameter name to the second column
                data.append(field)
    return data


def generate_csv_semantic_model(data_model_path, semantic_model_path, field_names):
    '''
    Extract data objects from a Data Model graphviz file, convert them to a csv table and backup csv file before saving.
    '''
    data_objects = pgv.parse_data_model(data_model_path)
    data = nodes2table(data_objects, field_names)

    # Backup
    date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    python_file_backup = '%s_%s' % (semantic_model_path, date)
    shutil.copyfile(semantic_model_path, python_file_backup)

    # save dictionary to a csv file
    with open(semantic_model_path, 'w') as csvfile:    
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)
     

if __name__ == '__main__':
    data_model_path = pathlib.Path('Data_Model/Data_Model.gv')
    semantic_model_path = pathlib.Path('Semantic_Model/Semantic_Model.csv')
    field_names = ['Object name', 'Parameter name', 'Type', 'Description']

    generate_csv_semantic_model(data_model_path, semantic_model_path, field_names)

