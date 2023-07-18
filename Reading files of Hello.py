# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 12:44:24 2022

@author: Abhik
"""

employee_file=open("Hello.txt","r+")

print(employee_file.readable())  #Checks if text is readable or not
print(employee_file.read())   #Reads the text




for employee in employee_file.readlines():
    print(employee)  #Assign data in list

employee_file.close()

