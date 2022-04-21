#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json         # JSON encoder and decoder
import pydot        # Python interface to Graphviz's Dot language
import datetime     # Basic date and time types
import shutil       # High-level file operations


def generate_data_model(json_file, gv_file):
    ''' Extract Data Model from ontology JSON file and convert to a GraphViz file'''
    
    # create a GraphViz's Dot object with the 'node' definition
    graph = pydot.Dot('datamodel', graph_type = 'digraph', colorscheme='pastel19')
    graph.add_node(pydot.Node('node', shape = 'record', style = 'filled, rounded', fillcolor = 'white', color = 'black'))

    # read ontology JSON file
    with open(json_file) as f:
        o = json.load(f)                    # ontology JSON format
        data = o['data']                    # Data Model
        count = 0                           # counter for Data Objects

        # Firstable, find data objects
        store_do = {}                       # to save data objects and their identifiers
        for i in data:
            count += 1
            do_id = 'o%d' % count           # identifier: o1, o2, o3...
            print('Data Object %s: "%s"' % (do_id, i))
            graph.add_node(             # create GraphViz's node for Data Object
                pydot.Node(do_id, label = i))
            store_do.update({i: do_id})

        print('\nThere are %s Data objects:\n' % (count))
    
        # Then, find relations between data objects
        count = 1
        for i in data:
            do = data[i]                        # Data Object
            print(i)
            if 'parent' in do:
                parents = do['parent']
                print('  parents:')
                for p in parents:
                    print('    - %s' % p)
                    graph.add_edge(
                        pydot.Edge('%s' % store_do[p], 'o%d' % count))
            if 'child' in do:
                childs = do['child']
                print('  childs:')
                for c in childs:
                    print('    - %s' % c)
            count += 1

    # backup existing files before generating new ones
    date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    shutil.copyfile(
        gv_file,                        # GraphViz file
        '%s_%s' % (gv_file, date))      # GraphViz file backup
    shutil.copyfile(
        '%s.png' % gv_file,             # PNG file
        '%s.png_%s' % (gv_file, date))  # PNG file backup

    # save graph and image to files
    graph.write(gv_file)                # GraphViz file
    graph.write_png('%s.png' % gv_file) # PNG file







# tests

def test_summary_ontology(json_file):
    with open(json_file) as f:
        o = json.load(f)
        
        # Scope Model
        scope = o['scope']
        activity_root = scope['root']
        root_title = scope['title']
        activities = scope['activities']
        means = scope['means']
        
        print('Scope Model:')
        print('  root "%s": "%s"' % (activity_root, root_title))
        print('  %d activities:' % len(activities))
        for i in activities:
            a = activities[i]
            print('    - %s: %s' % (i, a['label']))
        print('  %d means:' % len(means))
        for i in means:
            print('    - %s' % i)
        
        # Data Model
        data = o['data']
        print('Data Model:')
        print('  %d object data:' % len(data))
        for i in data:
            print('    - %s' % i)

        # Behaviour Model
        behaviour = o['behaviour']
        print('Behaviour Model:')
        print('  %d elementary activities:' % len(behaviour))
        for i in behaviour:
            print('    - %s' % i)




if __name__ == '__main__':
    json_file = 'ontology.json'
    gv_file = 'Data_Model/Data_Model.gv'

#    test_summary_ontology(json_file)
    generate_data_model(json_file, gv_file)
    
    
