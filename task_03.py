#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module Contains a Function for Lexicographical Analysis"""


def lexicographics(to_analyze):
    item = ''
    maximum = 0
    minimum = 0
    avg = 0
    for i in to_analyze:
        item += i
        item.split('\n')
    item = [item]
    print item
 
if __name__ == '__main__':
    print lexicographics('''Don't stop believing,\n Hold on to that feeling.''')
