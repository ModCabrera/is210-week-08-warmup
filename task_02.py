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
