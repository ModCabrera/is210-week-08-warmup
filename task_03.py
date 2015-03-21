#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module contains which function and does Lexicographical Analysis"""
import decimal


def lexicographics(to_analyze):
    """Function examines string for length words in lines, minimum, average.

    Args:
    to_analyze (str): string to be analyzed by words, lines.

    Returns:
    max_words (tup): Maximum length of words by line in string.
    min_words (tup): Minimum length of words by line in string.
    average (tup): Average length of words by line in string.

    Examples:
    >>> import task_03
    >>> import data
    >>> task_03.lexicographics(data.SHAKESPEARE)
    (12, 5, Decimal('8.14'))

    >>> import task_03
    >>> task_03.lexicographics('''Don't stop believing,
    Hold on to that feeling.''')
    (5, 3, Decimal(4.0))
    """
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
