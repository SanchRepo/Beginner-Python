# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 13:19:46 2017

@author: szh24
"""

from random import random
import math

attempts= raw_input("Number of attempts?  ")
hits=0
for i in range(int(attempts)):
    ytail= 2.0*random()
    randangle= math.pi*random()

    yhead = ytail + math.sin(randangle)

    if yhead>2:
        hits=hits+1
ratio=float(attempts)/hits 

print(ratio)       