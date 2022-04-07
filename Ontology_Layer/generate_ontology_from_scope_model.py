#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import shutil       # High-level file operations
import datetime     # Basic date and time types
import json


def parse_idl(idl_file):
    ''' Parse IDL file a return a dictionary '''
    
    with open(idl_file, 'r') as f:
        s = ' '.join(line.strip() for line in f)

    diagrams = s.split('DIAGRAM GRAPHIC')   # divide string into diagrams
    diagrams.pop(0)                         # remove header

    r = {}
    for d in diagrams:
        r.update(parse_idl_diagram(d))
    
    return r
    
def parse_idl_diagram(d):
    lines = d.split(';')
    graphic = lines.pop(0).strip()

    for line in lines:
        line = line.strip()
        if line.split(' ', 1)[0] == 'TITLE':
            title = line.split("'")[1::2][0]
    
    boxes  = re.findall(r' BOX (.*?)ENDBOX', d)
    arrows = re.findall(r'ARROWSEG (.*?)ENDSEG', d)
    bd, ad = {}, {}
    for b in boxes:
        r = parse_idl_box(b)
        bd.update(r)
    for a in arrows:
        r = parse_idl_arrow(a)
        ad.update(r)

#    r = {'diagram': graphic, 'title': title, 'boxes': bd, 'arrows': ad}
    r = {graphic: {'title': title, 'boxes': bd, 'arrows': ad}}
#    print(json.dumps(r, indent=4))
    return r

def parse_idl_box(b):
    lines = b.split(';')
    num = lines.pop(0).strip()
#    print('num  = "%s"' % num)
    for i in lines:
        i = i.strip()
        first = i.split(' ', 1)[0]
        if first == 'NAME':
            name = i.split("'")[1::2][0]
            name = name.split("}")[-1]
            name = name.replace('<CR>', ' ')
#            print('name = "%s"' % name)
        if first == 'DETAIL':
            detail = i.split(' ')[-1]
#            print('detail = "%s"' % detail)
    return {num: {'name': name, 'detail': detail}}

def parse_idl_arrow(a):
    lines = a.split(';')
    num = lines.pop(0).strip()
#    print('num  = "%s"' % num)
    for i in lines:
        i = i.strip()
        first = i.split(' ')[0]
        
        if first == 'SOURCE':
            words = i.split(' ')
            node = words[1]
            if node == 'BORDER' or node == 'TUNNEL':
                s = {'node': node}
            elif node == 'BOX':
                arrow_type = ''.join(filter(str.isalpha, words[2]))
                box = words[2].split(arrow_type)[0]
                s = {'node': node, 'type': arrow_type, 'box': box}
            elif node == 'BRANCH' or node == 'JOIN':
                arrows = words[2:]
                s = {'node': node, 'arrows': arrows}
            else:
                s=None
#            print(s)
                
        if first == 'LABEL' and i.split(' ')[1] != 'COORDINATES':
            label = i.split("'")[1::2][0]
            label = label.split("}")[-1]
            label = label.replace('<CR>', ' ')
#            print(label)

        if first == 'SINK':
            words = i.split(' ')
            node = words[1]
            if node == 'BORDER' or node == 'TUNNEL':
                d = {'node': node}
            elif node == 'BOX':
                arrow_type = ''.join(filter(str.isalpha, words[2]))
                box = words[2].split(arrow_type)[0]
                d = {'node': node, 'type': arrow_type, 'box': box}
            elif node == 'BRANCH' or node == 'JOIN':
                arrows = words[2:]
                d = {'node': node, 'arrows': arrows}
            else:
                d=None
#            print(d)
                
    r = {num: {'source': s, 'label': label, 'sink': d}}
#    print(r)
    return r


def idl2mfm(json_file):
    ''' Convert a JSON file in IDL format to a dictionary-based MfM Scope Model '''

    scope_model = {}
    data_objects = {}
    behaviour_model = {}
    activities = {}
    means = {}

    with open(json_file) as f:
        data = json.load(f)

        # iterate on IDL diagrams
        for d in data:
            diagram = data[d]
#            print('Diagram %s: %s' % (d, diagram['title']))

            # parse IDL boxes as activities (with empty means, inputs and outputs)
            for b in diagram['boxes']:
                box = diagram['boxes'][b]
                activity_id = box['detail']
                activity_label = box['name']
                
#                print('  Box %s: %s' % (b, activity_label))
                activity = {activity_id: {
                    'label': activity_label, 
                    'means': [], 
                    'input': [], 
                    'output': [], 
                    }}
                    
                if d in activities:             # diagram is an activity: append parent and children
                    activity[activity_id].update({'parent': d})
                    parent = activities[d]
                    if not 'child' in parent:
                        parent.update({'child': [activity_id]})
                    else:
                        parent['child'].append(activity_id)
                    if d in behaviour_model:
                        behaviour_model.pop(d)
                    behaviour_model.update({activity_id: {}})
                else:                           # the single box in first diagram is root
                    scope_model = {'root': activity_id, 'title': activity_label}
                    behaviour_model.update({activity_id: {}})
            
#                print(json.dumps(activity, indent=4))
                activities.update(activity)
            
                
            # parse IDL arrows as means and data objects
            # activities -> append means, inputs (IDL inputs + IDL controls) and outputs
            # means -> append activity labels
            # data objects -> append activity labels
            # branch, join -> dictionaries for parent-child relations, e.g.: {"4": ["11", "12"], ...}
            branch, join = {}, {}
            for a in diagram['arrows']:
                arrow = diagram['arrows'][a]
                arrow_label = arrow['label']
                src, dst = arrow['source'], arrow['sink']
                
                # parse IDL arrow destination
                if dst['node'] == 'BORDER' or dst['node'] == 'TUNNEL':
                    str2 = dst['node']
                elif dst['node'] == 'BOX':
                    arrow_type = dst['type']
                    arrow_box = dst['box']
                    str2 = 'BOX %s (type=%s)' % (arrow_box, arrow_type)

                    # activity destination
                    act_id = diagram['boxes'][arrow_box]['detail']
                    arrow_activity = activities[act_id]
#                    print('************************ %s, %s' % (act_id, arrow_activity))

                    # MECHANISM (SINK)
                    if arrow_type == 'M':

                        # means -> append activity labels
                        if not arrow_label in means:
                            ameans = {arrow_label: {}}
                            means.update(ameans)
                        if not 'activities' in means[arrow_label]:
                            ameans = {arrow_label: {'activities': [act_id]}}
                            means.update(ameans)
#                            print('Adding new means "%s" to activity "%s"' % (arrow_label, act_id))
                        else:
                            means[arrow_label]['activities'].append(act_id)
#                            print('Appending existing means "%s" to activity "%s"' % (arrow_label, act_id))

                        # activity -> append means label
                        if not arrow_label in arrow_activity['means']:
                            arrow_activity['means'].append(arrow_label)
#                            print('Appending new means "%s" to activity "%s"' % (arrow_label, act_id))

                    # INPUT & CONTROL (SINK)
                    elif arrow_type in ['I', 'C']:

                        # data object -> append activity labels
                        if not arrow_label in data_objects:
                            d_obj = {arrow_label: {'input': [act_id]}}
                            data_objects.update(d_obj)
#                            print('Adding new data object "%s": input to activity "%s"' % (arrow_label, act_id))
                        else:
                            d_obj = data_objects[arrow_label]
                            if not 'input' in d_obj:
                                d_obj['input'] = []
                            d_obj['input'].append(act_id)
                            data_objects.update({arrow_label: d_obj})
#                            print('Updating existing data object "%s": input to activity "%s"' % (arrow_label, act_id))

                        # activity -> append data object label
                        if not arrow_label in arrow_activity['input']:
                            arrow_activity['input'].append(arrow_label)
#                            print('Appending new input "%s" to activity "%s"' % (arrow_label, act_id))
                        
                    # OUTPUT (SINK)
                    elif arrow_type == 'O':
                        print('WARNING: "%s" should not be an arrow destination' % str2)
                    else:
                        print('WARNING: "%s" --> %s is not valid' % (str2, arrow_type))
                        
                elif dst['node'] == 'BRANCH':
                    branch.update({a: dst['arrows']})
                    str2 = 'arrow %s' % str(dst['arrows'])[1:-1]
#                    print('    Branch: from arrow %s to %s' % (a, str2))
                elif dst['node'] == 'JOIN':
                    str2 = 'union of arrows %s' % str(dst['arrows'])[1:-1]
                else:
                    str2 = 'WARNING! ----- %s' % dst['node']


                # parse IDL arrow source
                if src['node'] == 'BORDER' or src['node'] == 'TUNNEL':
                    str1 = src['node']
                elif src['node'] == 'BOX':
                    arrow_type = src['type']
                    arrow_box = src['box']
                    str1 = 'BOX %s (type=%s)' % (arrow_box, arrow_type)

                    # activity source
                    act_id = diagram['boxes'][arrow_box]['detail']
                    arrow_activity = activities[act_id]

                    # MECHANISM, INPUT & CONTROL (SOURCE)
                    if arrow_type in ('M', 'I', 'C'):
                        print('WARNING: "%s" should not be an arrow source' % str1)

                    # OUTPUT (SOURCE)
                    elif arrow_type == 'O':

                        # data object -> append activity labels
                        if not arrow_label in data_objects:
                            d_obj = {arrow_label: {'output': [act_id]}}
                            data_objects.update(d_obj)
#                            print('Adding new data object "%s": output to activity "%s"' % (arrow_label, act_id))
                        else:
                            d_obj = data_objects[arrow_label]
                            if not 'output' in d_obj:
                                d_obj['output'] = []
                            d_obj['output'].append(act_id)
                            data_objects.update({arrow_label: d_obj})
#                            print('Updating existing data object "%s": output to activity "%s"' % (arrow_label, act_id))

                        # activity -> append data object label
                        if not arrow_label in arrow_activity['output']:
#                            print('Appending new output "%s" to activity "%s"' % (arrow_label, act_id))
                            arrow_activity['output'].append(arrow_label)

                    else:
                        print('WARNING: "%s" --> %s is not valid' % (str1, arrow_type))

                elif src['node'] == 'BRANCH':
                    str1 = 'arrow %s' % src['arrows'][0]
#                    print('    Arrow %s: from %s to %s' % (a, str1, str2))
                elif src['node'] == 'JOIN':
                    join.update({a: src['arrows']})
                    str1 = 'arrow %s' % str(src['arrows'])[1:-1]
#                    print('    Join: from %s to arrow %s' % (str1, a))
                else:
                    str1 = 'WARNING! ----- %s' % src['node']

#                print('    Arrow %s: from %s to %s' % (a, str1, str2))
    
    
            # PARENT-CHILD RELATIONS
            for b in branch:
                parent_label = diagram['arrows'][b]['label']
                for child in branch[b]:
                    child_label = diagram['arrows'][child]['label']
                    child_type = diagram['arrows'][child]['sink']['node']
                    if parent_label != child_label and child_type != 'JOIN':
                        if parent_label in means:
                            p = means[parent_label]
                            if not 'child' in p:
                                p['child'] = [child_label]
                            else:
                                p['child'].append(child_label)

                            c = means[child_label]
                            c['parent'] = parent_label
#                            print('Branch: means "%s" is parent of "%s"' % (parent_label, child_label))
                        else:
                            p = data_objects[parent_label]
                            if not 'child' in p:
                                p['child'] = [child_label]
                            else:
                                p['child'].append(child_label)

                            c = data_objects[child_label]
                            c['parent'] = parent_label
#                            print('Branch: data object "%s" is parent of "%s"' % (parent_label, child_label))

            for j in join:
                parent_label = diagram['arrows'][j]['label']
                for child in join[j]:
                    child_label = diagram['arrows'][child]['label']
                    child_type = diagram['arrows'][child]['sink']['node']
                    if parent_label != child_label:
                        if parent_label in means:
                            p = means[parent_label]
                            if not 'child' in p:
                                p['child'] = [child_label]
                            else:
                                p['child'].append(child_label)

                            c = means[child_label]
                            c['parent'] = parent_label
#                            print('Join: means "%s" is parent of "%s"' % (parent_label, child_label))
                        else:
                            if not child_label in data_objects:
                                d_obj = {child_label: {'parent': parent_label}}
                                data_objects.update(d_obj)
                            else:
                                p = data_objects[parent_label]
                                if not 'child' in p:
                                    p['child'] = [child_label]
                                else:
                                    p['child'].append(child_label)

                            c = data_objects[child_label]
                            c['parent'] = parent_label
#                            print('Join: data object "%s" is parent of "%s"' % (parent_label, child_label))
    


    scope_model.update({'activities': activities, 'means': means})
    
    return {
        'scope': scope_model, 
        'data': data_objects, 
        'behaviour': behaviour_model, 
        }
    

def generate_ontology(idl_file, json_file):
    r = parse_idl(idl_file)
    
    # parse IDL format to JSON file
    json_file1 = '%s.json' % idl_file
    with open(json_file1, 'w') as f:
        json.dump(r, f)

    # convert to MfM ontology and save to JSON file
    r = idl2mfm(json_file1)
    with open(json_file, 'w') as f:
        json.dump(r, f)








# tests

def test_idl2json(idl_file, json_file, text_file):
    r = parse_idl(idl_file)
    with open(json_file, 'w') as f:
        json.dump(r, f)
    with open(text_file, 'w') as f:
        f.write('"This file has been generated from idl_parser_to_dictionary.py"\n')
        f.write('"For testing purposes only."\n\n')
        f.write(json.dumps(r, indent=4))

def test_summary_json(json_file):
    with open(json_file) as f:
        data = json.load(f)
        
        for d in data:
            diagram = data[d]
            print('Diagram %s: %s' % (d, diagram['title']))
            for b in diagram['boxes']:
                box = diagram['boxes'][b]
                print('  Box %s: %s' % (b, box['name']))
            for a in diagram['arrows']:
                arrow = diagram['arrows'][a]
                src, dst = arrow['source'], arrow['sink']

                if src['node'] == 'BORDER' or src['node'] == 'TUNNEL':
                    str1 = src['node']
                elif src['node'] == 'BOX':
                    str1 = 'BOX %s (type=%s)' % (src['box'], src['type'])
                elif src['node'] == 'BRANCH':
                    str1 = 'arrow %s' % src['arrows'][0]
                elif src['node'] == 'JOIN':
                    str1 = 'union of arrows %s' % str(src['arrows'])[1:-1]
                else:
                    str1 = 'WARNING! ----- %s' % src['node']

                if dst['node'] == 'BORDER' or dst['node'] == 'TUNNEL':
                    str2 = dst['node']
                elif dst['node'] == 'BOX':
                    str2 = 'BOX %s (type=%s)' % (dst['box'], dst['type'])
                elif dst['node'] == 'BRANCH':
                    str2 = 'arrow %s' % str(dst['arrows'])[1:-1]
                elif dst['node'] == 'JOIN':
                    str2 = 'union of arrows %s' % str(dst['arrows'])[1:-1]
                else:
                    str2 = 'WARNING! ----- %s' % dst['node']

                print('  Arrow %s: from %s to %s' % (a, str1, str2))
        
def test_idl2mfm(json_file1, json_file2, text_file):
    r = idl2mfm(json_file1)
    with open(json_file2, 'w') as f:
        json.dump(r, f)
    with open(text_file, 'w') as f:
        f.write('"This file has been generated from idl_parser_to_dictionary.py"\n')
        f.write('"For testing purposes only."\n\n')
        f.write(json.dumps(r, indent=4))





if __name__ == '__main__':
    idl_file = 'Scope_Model/Scope_Model.idl'

    text_file1 = 'example - 1 parsing IDL format.txt'
    json_file1 = 'example - 1 parsing IDL format.json'
    text_file2 = 'example - 2 from IDL to MfM ontology.txt'
    json_file2 = 'example - 2 from IDL to MfM ontology.json'
    
#    test_idl2json(idl_file, json_file1, text_file1)
#    test_summary_json(json_file1)
#    test_idl2mfm(json_file1, json_file2, text_file2)
    
    json_file = 'ontology.json'    
    generate_ontology(idl_file, json_file)
    
