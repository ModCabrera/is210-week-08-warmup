#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module Contains a Function for Lexicographical Analysis"""
import decimal

def lexicographics(to_analyze):
    list_of_sentences = to_analyze.split('\n')
    max_words = 0
    min_words = len(list_of_sentences[0].split())
    total_words = 0
    for sentence in list_of_sentences:
        numwords = len(sentence.split())
        if numwords > max_words:
            max_words = numwords
            
        if numwords <= min_words:
            min_words = numwords
        total_words += numwords
    average = total_words/decimal.Decimal(len(list_of_sentences))
    return max_words, min_words, average

if __name__ == '__main__':
    import data
    print lexicographics(data.SHAKESPEARE)
