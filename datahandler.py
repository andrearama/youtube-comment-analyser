# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:24:35 2018

@author: Andrea Ramazzina
"""
import csv


def import_comments(file_name): 
    """
    Extract a list of the comments from the csv data file.
    """    
    
    if 'csv' not in file_name:
        file_name = file_name + '.csv'
    
    failed_retrivials_number = 0
    comments = [];
    with open('data.csv',encoding="utf8") as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            for count,element in enumerate(row):
                # The comment text is two indexes after the time
                if 'ago' in element:
                    try:
                        comments.append(row[count+2])
                    except IndexError:                
                        failed_retrivials_number = failed_retrivials_number+1
                    break
    
    print('Total number of comments successfully extracted:'+ str(len(comments)-failed_retrivials_number))   
    print('Total number of comments unsuccessfully extracted:'+ str(failed_retrivials_number))        

    return comments     
