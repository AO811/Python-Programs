# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 12:45:44 2022

@author: Abhik
"""

n=int(input("Enter a number: "))
t=n
num=0
p=True
while(p==True):
    sum=0
    while(t>0):
      r=t%10
      sum=sum+(r*r)
      t=t//10
    if(sum<10):
      num=sum
      p=False
    else:
        t=sum
        continue

if(num==1):
    print("Happy")
else:
    print("Not")
    