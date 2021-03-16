# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 18:35:42 2017

@author: Sancheet Hoque
"""

def Fib(end):
    a=1
    b=1
    fib_numbers=[a,b]
    for i in range(end-2):
        sum_fib=a+b
        fib_numbers.append(sum_fib)
        a=b
        b=sum_fib
        
    return fib_numbers

for i in Fib(20):
    print i
    
