# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 20:41:06 2022

@author: Abhik
"""

print("Python program to reverse a number.")
a=int(input("Enter a number: "))
rev=0
while(a!=0):
    rev=rev*10
    rev=rev+(a%10)
    a=int(a/10)
print(rev)    
    
        
    