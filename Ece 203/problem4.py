# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 13:08:51 2017

@author: szh24
"""

a = 3.3 
b = 5.3
a2 = a**2
b2 = b**2
eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2
eq1_pow = (a + b)**2
eq2_pow = (a - b)**2
print ('1st equation: %f = %f' %(eq1_sum, eq1_pow))
print ('2nd equation: %f = %f' %(eq2_pow, eq2_pow))



