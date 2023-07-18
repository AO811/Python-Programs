# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:21:49 2022

@author: Abhik
"""
from Inheritance_chef_class_Part_I import chef  #THIS IS WHERE INHERITANCE TAKES PLACE
class Chinese_chef(chef):           #chef class is inherited by Chinese_chef class
    
        
    def make_special_dish(self):
        print("The Chinese chef makes chowmein")
        
    def make_fried_rice(self):
        print("The Chinese chef makes fried rice")
        