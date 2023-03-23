#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Domingo Morales Palma <dmpalma@us.es>
"""

def check_for_specimen(t0, d0):
    print('To perform the experimental test, a specimen is required with a %f-mm sheet thickness and a %f-mm hole diameter.' % (t0, d0))
    is_prepared = input('Has the specimen already been manufactured? ')
    is_prepared = is_prepared.lower()
    if is_prepared in ['yes', 'y']:
        print('Ok, task completed.')
    elif is_prepared in ['no', 'n']:
        print('Ok. Please note that this task has not been completed yet.')
    else:
        print('Answer not valid.')
        is_prepared = ''
    return is_prepared

if __name__ == '__main__':
    t0 = 1.6
    d0 = 58
    ip = check_for_specimen(t0, d0)
    print("Returned is_prepared = '%s'" % ip)
