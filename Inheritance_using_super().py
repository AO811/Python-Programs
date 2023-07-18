# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 15:20:13 2022

@author: Abhik
"""

class Vehicle():
    def _init_(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    def show_details(self):
        print("I am Vehicle")
        print("The mileage is",self.mileage)
        print("The cost is",self.cost)
        
class Car(Vehicle):
    def _init_(self,mileage,cost,tyres,hp):
        super()._init_(mileage, cost)
        self.tyres=tyres
        self.hp=hp
    def show_car_details(self):
        print("I am a car")
        print("The tyres is",self.tyres)
        print("The hp is",self.hp)
        print("The mileage is",self.mileage)
        print("The cost is",self.cost)
        
c1=Car()
c1._init_(50,500000,8,200)
print(c1.show_details())
print(c1.show_car_details())
        
        