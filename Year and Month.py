# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 21:54:28 2022

@author: Abhik
"""

#5.Python program to print the calendar of a given month and year
import calendar
yr = int(input("Enter the year(in numbers): "))
mo = int(input("Enter the month(in numbers): "))
print(calendar.month(yr, mo))
