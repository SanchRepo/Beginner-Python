# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 13:51:09 2017

@author: szh24
"""

class Bug:
    
    def __init__(self,initialPosition):
        self.initialPosition = float(initialPosition)
        self.pot=1
        
    def move(self):
        self.initialPosition+=self.pot

    def turn(self):
        self.pot=self.pot*-1

        
    def position(self):
        return self.initialPosition  
        
    def direction(self):
        if self.pot==1:
            print("Bug is facing right")
        elif self.pot==-1:
            print("Bug is facing left")
            
            
ant = Bug(10) # starts at position 10 facing right
ant.move() # Position is 11
ant.turn() # now facing left
ant.move() # Position is 10
ant.move() # Position is 9
print ant.position() # prints ‘9’ to the screen
print ant.direction() # prints ‘left’ to the screen           