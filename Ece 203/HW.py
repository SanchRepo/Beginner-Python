# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 13:41:01 2017

@author: szh24
"""
name={}
F=[i*10 for i in range (11)]
C=[]
for j in range(11):
   value=(5.0/9.0)*(F[j]-32)
   value=float("{0:.2f}".format(value))
   C.append(value)
    
    

name["celcius"]=C
name["fahrenheit"]=F

print("| Fahrenheit | Celcius |")
for l in range(11):
    if len(str(F[l]))==1:
        print('|     {0}      |  {1} | '.format(F[l],C[l]) )
        
    elif len(str(F[l]))==3:
        print('|     {0}    |   {1} | '.format(F[l],C[l]) )
        
    else:   
        print('|     {0}     |    {1} | '.format(F[l],C[l]) )
    

