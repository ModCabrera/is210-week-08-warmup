#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Small function which returns 'yes','no' equivalent to truthy,falsy"""


def bool_to_str(bval):
    """Function evaluates truthy or falsy values and returns string equivalent.

    Args:
    bval (str, list, tup, int): Variable and evals truthy or falsy.

    Returns:
    bval (str): bval returns 'yes' if true, else 'no' if false.

    Examples:
    >>> import task_02
    >>> task_02.bool_to_str(True)
    'Yes'

    >>> import task_02
    >>> task 02.bool_to_str('')
    'No'
    """
    truthy = 'Yes'
    falsy = 'No'
    if bval and True:
        bval = truthy
    else:
        bval = falsy
    return bval
