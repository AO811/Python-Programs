# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 13:02:58 2022

@author: Abhik
"""

#season={"Spring":["March","April","May"],"Summer":["June","July","August"],"Autumn":["September","October","November"],"Winter":["December","January","February"]}

n=int(input("Enter the month number: "))
if(n==1 or n==2 or n==12):
    print("Winter")
elif(n==3 or n==4 or n==5):
    print("Spring")
elif(n==6 or n==7 or n==8):
    print("Summer")
elif(n==9 or n==10 or n==11):
    print("Autumn")
else:
    print("Invlid Month")
    
    
                                         