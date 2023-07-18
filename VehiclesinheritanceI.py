# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 23:17:43 2022

@author: Abhik
"""

class Vehicle:
    def init(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    
    def show_details(self):
        print("I am a vehicle")
        print("The mileage is ",self.mileage)
        print("The cost is ",self.cost)
        
v1 = Vehicle(300,1000)
v1.show_details()        

        