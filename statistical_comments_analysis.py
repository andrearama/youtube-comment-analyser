# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 14:14:26 2018

@author: Andrea Ramazzina
"""

from nltk.tokenize import TweetTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize

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




def bag_of_words_sentence(sentence):
    """
    Return bag of words extracted from the sentence (word count)
    Input: TextBlob object
    Output: defaultdict object
    """
    print("Attention: the values are the words count, not frequency")
    bag = sentence.word_counts
    return bag

def bag_of_words_corpus(corpus):
    """
    Return bag of words extracted from the sentence
    Input: List of sentences
    Output: List of lists containing the frequency of each word
    """    
    vectorizer = CountVectorizer()
    features = vectorizer.fit_transform(corpus).todense() 
    features_norm = normalize(features, axis=1, norm='l1')
    return features_norm
   
    #from sklearn.metrics.pairwise import euclidean_distances
    #    print(euclidean_distances(features[0],f))
        
        
        
        
        
        