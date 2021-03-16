# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 12:59:03 2017

@author: szh24
"""
import math

class SodaCan:
    
    def __init__(self,height,radius):
        self.height = float(height)
        self.radius = float(radius)
        self.surfacearea=0
        self.volume=0
        
    def getSurfaceArea(self):
        self.surfacearea=2*math.pi*self.height*self.radius+2*math.pi*self.radius**2
        return self.surfacearea      
    def getVolume(self):
        self.volume=math.pi*self.radius**2*self.height
        return self.volume 

        
        



        
boi = SodaCan(4,4)        

print boi.getVolume()
print boi.getSurfaceArea()
