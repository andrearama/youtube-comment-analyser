# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 14:14:26 2018

@author: andre
"""

import nltk
from nltk.tokenize import TweetTokenizer



def compute_lexical_diversity(comments):
    """
    First estimation of the lexical diversity of the comments      
    """    
    tknzr = TweetTokenizer()
    
    text = ''
    for element in comments:
        text = text+element
    
    word_list = tknzr.tokenize(text)
    lexical_diversity = len(set(word_list))/len(word_list)
    return lexical_diversity