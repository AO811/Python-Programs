# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 21:41:23 2022

@author: Abhik
"""
#3.Python program that accepts an integer (say n) and computes the value of n+nn+nnn
n = int(input("Enter an integer: "))
n1 = int( "%s" % n )
n2 = int( "%s%s" % (n,n) )
n3 = int( "%s%s%s" % (n,n,n) )
print ("The required sum: "+ str(n1+n2+n3))
