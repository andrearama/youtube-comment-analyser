# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 12:50:48 2018

@author: Andrea Ramazzina
"""
from datahandler import *
from statistical_comments_analysis import *

comments = import_comments('data.csv')             

lexical_diversity = compute_lexical_diversity(comments)
print(lexical_diversity)
