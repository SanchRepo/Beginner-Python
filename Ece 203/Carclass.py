# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 13:32:51 2017

@author: szh24
"""

class Car:
    
    def __init__(self,eff):
        self.eff = float(eff)
        self.fuel = 0
    
        
    def drive(self,distance):
        if self.eff*self.fuel >= distance:
            self.fuel-= float(distance)/self.eff
            
            return True
        else:
            return False

    def get_gas_level(self):
        
        return self.fuel
        
    def add_gas(self,amount):
        self.fuel+=amount
        
        
hybrid_car = Car(50) # 50 miles per gallon
hybrid_car.add_gas(20) # Add 20 gallons of fuel
if hybrid_car.drive(100): # Drive 100 miles
    print hybrid_car.get_gas_level() # Display remaining fuel
else:
    print "Not enough gas!"
        