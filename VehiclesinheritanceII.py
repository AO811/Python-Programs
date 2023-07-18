# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 23:32:21 2022

@author: Abhik
"""
from VehiclesinheritanceI import Vehicle
class Car(Vehicle):
    def show_car_details(self):
        print("I am a car")
        
c1=Car(100,2000)
c1.show_details()