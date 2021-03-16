# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 13:31:28 2017

@author: szh24
"""

def Refrac(R1,R2,d,n):
    R1=float(R1)
    R2=float(R2)
    d=float(d)
    n=float(n)    
    
    fin=(n-1)*((1.0/R1)-(1.0/R2)+(((n-1)*d)/(n*R1*R2)))
    f=1.0/fin
    
    return f