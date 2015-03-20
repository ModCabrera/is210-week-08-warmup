#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fibonnaci Docstring"""


def fibonacci(maxint):
    a,b = 0,1
    fib = [0]
    while b < maxint:
        fib.append(b)
        a,b = b, a+b
    return fib

if __name__ == '__main__':
    print fibonacci(10)
