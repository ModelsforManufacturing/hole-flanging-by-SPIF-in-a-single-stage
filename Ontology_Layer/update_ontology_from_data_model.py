#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib      # Object-oriented filesystem paths
import json         # JSON encoder and decoder
import datetime     # Basic date and time types
import shutil       # High-level file operations
import parse_graphviz_data_model as pgv

def update_format_dictionary(dictionary):
    ''' Capitalize the keys of a dictionary '''
    #Format Function
    keylistold=list(dictionary.keys())                          # extract keys
    keylistnew=[]
    for i in keylistold:
        key_old=i.split(' ')                                    # split key into words
        count=[]
        for j in range (0,len(key_old)):
            aux2=key_old[j].strip()
            if not aux2 == 'and' and aux2[0].isupper()==False:  # if word is not capitalized
                count.append(aux2[0].upper() + aux2[1:])        # capitalize the word
            else:
                count.append(aux2)
        key_new=count[0]
        for k in range (1,len(count)):
            key_new=key_new+' '+count[k]
        keylistnew.append(key_new)
        if i!=key_new:                                          # if key has changed
            dictionary[key_new]=dictionary[i]                   # replace the key
            del dictionary[i]
    return dictionary

def update_ontology_from_data_model(json_path, gv_path):
    ''' Read enriched Data Model from GraphViz file to update the Ontology JSON file '''
    
    # parse enriched Data Model to a dictionary according to the MfM Metamodel
    data_objects = pgv.parse_data_model(gv_path)
    
    ontology = {}
    with open(json_path) as f:
        ontology = json.load(f)             # load ontology from JSON file as dictionary
        data = ontology['data']             # extract the Data Model
        
        # capitalize dictionary keys
        data=update_format_dictionary(data)
        data_objects=update_format_dictionary(data_objects)
        
        keys_old=list(data.keys())
        keys_new=list(data_objects.keys())
        
        # check inconsistencies in data object names
        data1=data.copy()
        for i in data:
            remove_final_letter = i[:-1]                        # e.g. plural to singular
            add_final_s = i+'s'                                 # singular to plural
            if remove_final_letter in keys_new:
                print('Warning: data object "%s" has been replaced by "%s"' 
                    % (i, remove_final_letter))
                data1[remove_final_letter] = data1[i]           # add new object name
                del data1[i]                                    # and remove old one
            if add_final_s in keys_new:
                print('Warning: data object "%s" has been replaced by "%s"' 
                    % (i, add_final_s))
                data1[add_final_s] = data1[i]                   # add new object name
                del data1[i]                                    # and remove old one
        data=data1.copy()    

        for i in data:
            if not i in keys_new:
                print('Warning: data object "%s" has been removed' % i)
                del data1[i]                                    # remove leftover object
        data=data1.copy()
        
        # Update 'data' with 'data_objects'
        #Option 1
        for i in data_objects:
             new=data_objects[i]
     
             if i in keys_old :
                 old=data[i]
                 old.update(new)
                   
                 data[i]=old                                     #update old key
             else:
                 data[i]=new                                     #add new key
        '''
        # Option 2
        for i in data_objects:
            new=data_objects[i]
    
            if i in keys_old :
                old=data[i]

                #update parent                
                newparent=[]
                if 'parent' in new:
                    if len(new['parent'])<2:
                        newparent=new['parent']
                    else:
                        for p in new['parent']:
                            newparent.append(p)
                    old.update({'parent': newparent})
                            
                            
                #update child                
                newchild=[]
                if 'child' in new:
                    if len(new['child'])<2:
                        newchild=new['child']
                    else:
                        for p in new['child']:
                            newchild.append(p)
                    old.update({'child': newchild})
                            
                #update parameter                
                newparameter=[]
                if 'parameter' in new:
                    if len(new['parameter'])<2:
                        newparameter=new['parameter']
                    else:
                        for p in new['parameter']:
                            newparameter.append(p)
                    old.update({'parameter': newparameter})
                
                data[i]=old                                     #update old key
            else:                           
                data[i]=new                                     #add new key
         '''

        ontology.update({'data': data})                         # update Ontology
                
    #backup existing files before generating new ones
    date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    shutil.copyfile(
        json_path,                        # JSON file
        '%s_%s' % (json_path, date))      # JSON file backup  
    
    #save updated Ontology as JSON file
    with open(json_path, 'w') as f:
        json.dump(ontology, f)
    
        

if __name__ == '__main__':
    json_path = pathlib.Path('ontology.json')
    gv_path = pathlib.Path('Data_Model/Data_Model.gv')
    
    update_ontology_from_data_model(json_path, gv_path)

    
