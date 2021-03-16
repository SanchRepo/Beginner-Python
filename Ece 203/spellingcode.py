# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 13:51:30 2017

@author: szh24
"""

file2 = open('missing_words.txt', 'w')
for line in open('misspell.txt'):
    maryl = line.split()
    for word in maryl:    
        mary=word.rstrip('".?!,;:')
        mary = mary.lstrip('?:!.,;"')
        mary= mary.lower()
        
        for word in open('american-english'):     
            word=word.rstrip()
            word=word.lower()
            if mary == word:
                cor=1
#                print(mary)
                break
    
            else:
                cor=2
       
        if cor==2:
            print(cor)
            print(mary)
            print>> file2, mary   
            

file2.close() #closing file            
