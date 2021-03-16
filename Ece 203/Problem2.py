# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 11:55:07 2017

@author: szh24
"""

name={}
F=[i*10 for i in range (11)]
C=[]
A=[]
E=[]
for j in range(11):
   value=(5.0/9.0)*(F[j]-32)
   approx=(0.5)*(F[j]-30) 
   error=abs(value-approx)
   value=float("{0:.2f}".format(value))
   approx=float("{0:.2f}".format(approx))
   error=float("{0:.2f}".format(error))
   C.append(value)
   A.append(approx)
   E.append(error)
   
    
    

print("| Fahrenheit | Celcius | Approx | Error |")

for l in range(11):
    if len(str(F[l]))==1:
        print('|     {0}      |  {1} | '.format(F[l],C[l]) )
        
    elif len(str(F[l]))==3:
        print('|     {0}    |   {1} | '.format(F[l],C[l]) )
        
    else:   
        print('|     {0}     |    {1} | '.format(F[l],C[l]) )