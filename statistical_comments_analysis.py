# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 14:14:26 2018

@author: andre
"""

from nltk.tokenize import TweetTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import TextBlob
import textblob

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
    filtered_words = (word.stem() for word in word_list if word not in stopwords.words('english'))
    
    if output_type == 'TextBlob':
       return TextBlob(' '.join(filtered_words))
    elif output_type == 'tuple':
       return filtered_words
    elif output_type == 'string':
        return ' '.join(filtered_words)
    else:
        raise ValueError('Output tpye not understood')

def bag_of_words_sentence(sentence):
    """
    Return bag of words extracted from the sentence
    Input: TextBlob object
    Output: defaultdict
    """
    
    bag = sentence.word_counts
    return bag

def bag_of_words_corpus(corpus):
    """
    Return bag of words extracted from the sentence
    Input: List of sentences
    Output: List of lists containing the number of times for each word
    """    
    vectorizer = CountVectorizer()
    features = vectorizer.fit_transform(corpus).todense() 
    return features
   
    #from sklearn.metrics.pairwise import euclidean_distances
    #    print(euclidean_distances(features[0],f))
        
        
        
        
        
        