# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 12:50:48 2018

@author: Andrea Ramazzina
"""
from datahandler import *
from statistical_comments_analysis import *
from sentiment_analysis import *
from NLP import *

#comments = import_comments('data.csv')             

#lexical_diversity = compute_lexical_diversity(comments)
#print(lexical_diversity)

#positive,negative,neutral = determine_sentiment(comments[0:30])

sentence = 'Hello, my name is Andrea. Actually, I have two names: Andrea and Ren Nan.'
a =preprocess_sentence(sentence, output_type = 'TextBlob')

print(a)