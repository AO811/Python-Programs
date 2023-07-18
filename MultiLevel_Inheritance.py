# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:35:56 2022

@author: Abhik
"""

class Parent():
    
    def assign_name(self,name):
        self.name=name
    
    def show_name(self):
        return "My name is",self.name
    
class Child(Parent):
    
    def assign_age(self,age):
        self.age=age
        
    def show_age(self):
        return self.name,"is",self.age
    
class GrandChild(Child):
    
    def assign_gender(self,gender):
        self.gender=gender
        
    def show_gender(self):
        return "I am",self.gender
    
g1= GrandChild()

g1.assign_name("Anya")
g1.assign_age(6)
g1.assign_gender("Female")    

print(g1.show_name())
print(g1.show_age())
print(g1.show_gender())
    
    
    