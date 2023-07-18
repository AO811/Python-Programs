# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 21:22:41 2022

@author: Abhik
"""

#1.Program to display current date and time
from datetime import datetime
now = datetime.now()
dt = now.strftime("%d/%m/%y %H:%M:%S")
print("Date and Time:- "+dt)