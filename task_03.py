#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module Contains a Function for Lexicographical Analysis"""

def lexicographics(to_analyze):
    splitsent = to_analyze.split('\n')
    splitwords = to_analyze.split()
    maximum = max(len(splitsent),len(splitwords))
    minimum = min(len(splitsent),len(splitsent))
    average = float(len(splitwords)/len(splitsent)) 
    print maximum, minimum, average

if __name__ == '__main__':
    lexicographics('''Don't stop believing,
    Hold on to that feeling.''')
