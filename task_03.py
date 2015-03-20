#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module Contains a Function for Lexicographical Analysis"""

def lexicographics(to_analyze):
    lines = ''
    line2  = ''
    line3 = ''
    totalperline = 0
    total_lines = []
    lista_t= []
    for char in to_analyze:
        lines += char
        line2 = lines.split('\n')
        line3 = line2[0]
        line3.split()
        lista_t = line3.split()
        totalperline = len(lista_t)
    total_lines.append(totalperline)
    return total_lines

if __name__ == '__main__':
    print lexicographics('''Don't stop believing,
    Hold on to that feeling.''')
