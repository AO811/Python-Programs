# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 20:52:55 2022

@author: Abhik
"""

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
if(num1>num2):
    l=len(str(num1))+1
else:
    l=len(str(num2))+1
sum2=0
while(l>0):
    r1=num1%10
    r2=num2%10
    sum=r1+r2
    carry=sum//10
    sum2=sum2+carry
    num1=num1//10
    num2=num2//10
    
print("The sum of carries: ",sum2)    
                
    
    