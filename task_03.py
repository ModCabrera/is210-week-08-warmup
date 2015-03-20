#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module Contains a Function for Lexicographical Analysis"""


def lexicographics(to_analyze):
    lines = ''
    lineslist=[]
    for char in to_analyze:
        lines += char
        lineslist = (lines.split('\n'))
    print lineslist
    
if __name__ == '__main__':
    print lexicographics('''Don't stop believing,
Hold on to that feeling.''')
