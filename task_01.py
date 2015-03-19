#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fibonnaci Docstring"""


def fibonacci(maxint):
    a, b  = 0,1
    fiblist = []
    while b < maxint:
        
        a,b = b, a+b

if __name__ == '__main__':
    print fibonacci(10)

