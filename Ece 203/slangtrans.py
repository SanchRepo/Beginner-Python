# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 12:59:18 2017

@author: szh24
"""



def slangtrans(string):
    slangdict={'gr8': 'great',
           'btw': 'by the way',
           'imho': 'in my humble opinion',
           'jk': 'just kidding',
           'l8r':'later',
           'np':'no problem',
           'r':'are',
           'u': 'you',
           'y': 'why',
           'ttyl': 'talk to you later',
           'l8': 'late',
           'atm': 'at the moment',
           'lmk': 'let me know',
           'np': 'no problem',
           'tia':'thanks in advance',
           'brb':'be right back'
          }
    stringl=[]
    
    
    for word in string.split():

            stringl.append(word)
 
    for i in range(len(stringl)):           
        try:    
             if stringl[i][-1] in ".?!,;:":

                    puncheck= list(stringl[i])
                    punc=puncheck[-1]
                    puncheck=puncheck[:-1]
                    puncheck2=''.join(puncheck)
                    stringl[i]=slangdict[puncheck2]+punc
             else:                            
                 stringl[i]=slangdict[stringl[i]]
                 
                 
        except:
            stringl[i]=stringl[i]

    sentence= ' '.join(stringl)
    
    return sentence   
             