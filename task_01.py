#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fibonnaci Docstring"""


def fibonacci(maxint):
    """Fibonacci sequence generator returns new sequence as list.

    Args:
    maxint (int): Upper bound of sequence to generated.

    Returns:
    fib (list of int): New list of sequential intergers.

    Examples:
    >>> import task_01
    >>> task_01.fibonacci(10)
    [0, 1, 1, 2, 3, 5, 8]
    
    >>> import task_01
    >>> fibonacci(20)
    [0, 1, 1, 2, 3, 5, 8, 13]
    """
    lastnum, curnum = 0,1
    fib = [0]
    while curnum < maxint:
        fib.append(curnum)
        lastnum, curnum = curnum, lastnum+curnum
    return fib
