# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:19:34 2022

@author: Abhik
"""

class Dad():
    def str_one(self,str1):
        self.str1=str1
        
    def show_str_one(self):
        return self.str1
        print("22")
       
class Mom():
    def str_two(self,str2):
        self.str2=str2
        
    def show_str_two(self):
        print("33")
        return self.str2
    
class Child(Dad,Mom):
    def str_three(self,str3):
        self.str3=str3
        
    def show_str_three(self):
        print( self.str3)

d1=Child()
d1.str_one("Daddy")
d1.str_two("Mommy")
d1.str_three("Yay")

print(d1.show_str_one())
print(d1.show_str_two())
print(d1.show_str_three())
    
    
    