#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Small func that returns 'yes' or 'no' value = truthy or falsy"""


def bool_to_str(bval):
    yes = 'Yes'
    no = 'No'
    if bval and True:
        bval = yes
    else: bval = no
    return bval

if __name__ == '__main__':

    """falses"""

    print bool_to_str([])
    print bool_to_str(())
    print bool_to_str(False)
    print bool_to_str('')

    """thruths"""
    
    print bool_to_str('s')
    print bool_to_str((1,))
    print bool_to_str([1,2,3])
    print bool_to_str(1)
    
