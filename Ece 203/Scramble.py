# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 13:41:59 2017

@author: szh24
"""
import random
def scramble(word):
    wordl=list(word)
    index=random.randint(1,len(word)-2)
    index2=index
    while index == index2:
        index2=random.randint(1,len(word)-2) 
    store=wordl[index]
    wordl[index]=wordl[index2]
    wordl[index2]=store
    word=''.join(wordl)
    
    return word



def build_sentence(string):
    stringl=[]
    for word in string.split():
        if len(word)<4:
            stringl.append(word)
        else:
            stringl.append(scramble(word))
    sentence=' '.join(stringl) 
    
    return sentence
            
            