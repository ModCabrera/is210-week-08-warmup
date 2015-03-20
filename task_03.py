#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module Contains a Function for Lexicographical Analysis"""

def lexicographics(to_analyze):
    lines = ''
    line2  = ''
    line_new = ''
    lis_t= []
    for char in to_analyze:
        lines += char
        line2 = lines.split('\n')
        line_new = line2[0]
        line_new.split()
        lis_t = line_new.split()
        for item in lis_t:
            print item
if __name__ == '__main__':
    print lexicographics('''Don't stop believing,
    Hold on to that feeling.''')
