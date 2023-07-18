# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 21:44:04 2022

@author: Abhik
"""

class Student:
    
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        
    def on_honour_roll(self):
        if self.gpa>8.5:
            return True
        else:
            return False
        