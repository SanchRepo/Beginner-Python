# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 19:07:43 2017

@author: Sancheet Hoque
"""

    
A=[[10,20,30,40,50,60],
   [11,21,31,41,51,61],
   [12,22,32,42,52,62],
   [13,23,33,43,53,63],
   [14,24,34,44,54,64],
   [15,25,35,45,55,65],
   [16,26,36,46,56,66]]


transpose = [[j[i] for j in A] for i, _ in enumerate(A[0])]