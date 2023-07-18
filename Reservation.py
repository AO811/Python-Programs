# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 13:13:32 2022

@author: Abhik
"""
cost=0
num_ticket=int(input("Enter the no. of tickets:"))
if(num_ticket<5 and num_ticket>40):
    print("Minimum of 5 and Maximum of 40 Tickets")
else:    
 refresh=str(input("Do you want refreshments:"))
 if(refresh.lower()=='y' or refresh.lower()=='yes' or refresh.lower()=='true' or refresh.lower()=='yeah'):
    cost=cost+num_ticket*50
 c=str(input("Enter the circle:"))
 if(c=='k'):
    cost=cost+num_ticket*75
 elif(c=='q'):
    cost=cost+num_ticket*150
 else:
    print("Invalid Input")
      
 coupon=str(input("Do you have coupon code:")) 
 if(coupon.lower()=='y' or coupon.lower()=='yes' or coupon.lower()=='true' or coupon.lower()=='yeah'):
    cost=cost-(cost*(2/100))
 if(num_ticket>20):
     cost=cost-(cost*(10/100))
     
print("Ticket cost:",cost)     