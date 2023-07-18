# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 22:57:27 2022

@author: Abhik
"""
n=5
 # number of spaces
k = n - 1
 
    # outer loop to handle number of rows
for i in range(0, n):
     
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
     
        # decrementing k after each loop
        k = k - 1
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("*", end=" ")
     
        # ending line after each row
        print()
 
n=5
 # number of spaces
k = 0
 
    # outer loop to handle number of rows
for i in range(n,0,-1):
     
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
     
        # decrementing k after each loop
        k = k + 1
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i):
         
            # printing stars
            print("*", end=" ")
     
        # ending line after each row
        print()