# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 22:32:20 2022

@author: Abhik
"""
from Classes_and_objects_PART_I import Student
     #file name                         #class name    
student1= Student("Abhik","CSE",9.5,False)
student2= Student("Alekhya","Commerce",9.5,False)

print(student1.name) 
print(student1.gpa) 
print(student2.name) 
print(student2.gpa) 

print(student1.on_honour_roll())
print(student2.on_honour_roll())
