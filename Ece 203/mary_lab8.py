# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#f=open('mary.txt')
#marylist= f.readlines()
#f.close

dict={}

for line in open('mary.txt'):
    maryl = line.split()
    for word in maryl:    
        mary=word.rstrip('".?!,;:')
        mary = mary.lstrip('?:!.,;"')
        mary= mary.lower()
        
        if mary not in dict:
            dict[mary]=1;
        else:
            dict[mary]=dict[mary]+1
            
            
for i in dict:
    print( i + ' : ' + str(dict[i]))
