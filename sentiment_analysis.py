# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 14:37:09 2018

@author: andre
"""

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



def determine_sentiment(comments, mode='vader'):
    '''
    Split the comment list in either positive, negative or neutral categories
    '''
    positive=[]
    negative = []
    neutral = []
    if mode == 'textblob':
        for comment in comments:
            analysis = TextBlob(comment)
            if analysis.sentiment.polarity>0.51:
                positive.append(comment)
            elif analysis.sentiment.polarity<-0.51:
                negative.append(comment)
            else:
                neutral.append(comment)
    
    elif mode == 'vader':     
        analyzer = SentimentIntensityAnalyzer()        
        for comment in comments:
            sentiment = analyzer.polarity_scores(comment)
    
            if sentiment['neg'] < 0.1:
                if sentiment['pos']-sentiment['neg'] > 0:
                    positive.append(comment)
                else:
                    neutral.append(comment)
                    
            elif sentiment['pos'] < 0.1:
                if sentiment['neg']- sentiment['pos'] > 0:
                    negative.append(comment)
                else:
                    neutral.append(comment)
                    
            else:
                neutral.append(comment)                
    else:
        raise NameError('Mode not detected. \n Please select a suitable mode (default: vader)') 
    return positive,negative,neutral             