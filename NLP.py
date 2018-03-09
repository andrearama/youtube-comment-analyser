# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 13:02:19 2018

@author: andre
"""
from nltk.corpus import stopwords
from textblob import TextBlob
import textblob

def preprocess_sentence(sentence, output_type = 'TextBlob'):
    """
    Put in lowecase filter out stopwords and stem a single sentence
    Input: String or TextBlob object 
    """
    if type(sentence) == str:
        sentence = TextBlob(sentence)
    elif type(sentence) != textblob.blob.TextBlob:
         raise ValueError('Input is neither a string or a TextBlob object')
           
    sentence = sentence.lower()
    word_list = sentence.words
    filtered_words = [word.stem() for word in word_list if word not in stopwords.words('english')]
    
    if output_type == 'TextBlob':
       return TextBlob(' '.join(filtered_words))
    elif output_type == 'list':
       return filtered_words
    elif output_type == 'string':
        return ' '.join(filtered_words)
    else:
        raise ValueError('Output tpye not understood')