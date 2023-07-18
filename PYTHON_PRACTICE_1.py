# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:00:48 2023

@author: Abhik
"""

"""
str=input("Enter a string:")
s=""
for i in range(len(str)-1,-1,-1):
  if (str[i]==" "):
      continue
  else:  
      r=str[i]
      s=s+r
if str.replace(" ","")==s:
    print("Palindrome string")
else:
    print("Not")    
"""

"""
def perf(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    if(sum==num):
        return True
    else:
        return False

for i in range(1,100001):
    if perf(i)==True:
        print(i)
"""

"""        
a=list()
l=int(input("Enter no. of elements"))
for i in range(l):
    e=int(input())
    if e>=1 and e<=30:
        a.append(e)

b=[]
for i in range(len(a)):
    b.append(a[i]*a[i])

print(b)    
"""

"""
def Even(lst):
    even=list()
    for i in range(len(lst)):
        if lst[i]%2==0:
            even.append(lst[i])
    return even

a=list()
l=int(input("Enter no. of elements"))
for i in range(l):
    e=int(input())
    a.append(e)
print("Even list:",Even(a))        
"""

"""
d=dict()
l=int(input("Limit:"))
for i in range(l):
    k=input("Key:")
    v=input("Value:")
    d[k]=v
print(d)    
"""

"""  
d=dict()
for i in range (3):
  k,v=input("Key:Value=").split(":")
  d[k]=v
"""

"""
d=dict()
l=int(input("Enter limit:"))
for i in range(l):
    k,v=input("Key:Value=").split(":")
    d[k]=v
print(d)
print(len(d))
k1=input("Enter the key you want to delete:")
if k1 in d.keys():
    del d[k1]
    print(d)
else:
    print("Key not found")
"""

"""
d=dict()
p=2
k=1
while(k<=100):
    c=0
    for j in range(1,p+1):
        if p%j==0:
            c+=1
    if c==2:
        d[k]=p
        k+=1
    p+=1 
print(d)    
"""

"""
d={"PHY":83,"CHE":87,"MAT":81}
d1=sorted(d.values(),reverse=True)
d2=dict()
for val in d1:
    for x in d:
       if d[x]==val:
           d2[x]=val
print(d2)           
"""  

"""
import numpy as np
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])  
c=list()
for i in range(len(a)):
    c.append(a[i]+b[i])
print(c)    
"""

"""
import numpy as np
a=np.array([[2,4],[6,8]])
b=np.array([[3,5],[7,9]])
c=np.concatenate((a,b),axis=None)
print(c)
"""

"""
import numpy as np
a=np.array([3,1,8,6,5,2],ndmin=2,dtype='f')
print(a)
print(sorted(a))
print(np.sort(a))
print(np.cumsum(a))
"""

"""
import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[6,7],[8,9]])
print(np.add(a,b))
print(np.subtract(a,b))
print(a+b)
print(a-b)
print(np.multiply(a,b))
print(a*b)
print(np.dot(a,b))
print(np.divide(a,b))
print(a/b)
print(a//b)
"""

"""
import numpy as np
a=np.array([[2,4],[6,8]])
d=np.linalg.det(a)
print(d)
print(int(d))
print(a.transpose())
print(np.linalg.inv(a))
"""

"""
print("     1 2 3 4 5 6 7 8 9 10")
print("-------------------------")
for i in range(1,11):
    print(i," |",end=" ")
    for j in range(1,11):
        print(i*j,end=" ")
    print()    
"""

"""
m=open("New_Av.txt","w")
m.write('''Abhik
Das''')
print(m.encoding)
print(m.mode)
print(m.name)
m.close()
print(m.closed)
"""

"""
from os import path
x=path.isfile("NEW_AVENGER.txt")
print(x)
mcu=open("NEW_AVENGER.txt","r")
print(mcu.readlines())
"""

"""
mcu=open("NEW_Avenger.txt","r")
for line in mcu:
    print(line,end="")
mcu.close()    
"""

"""
num_lines=num_words=num_letters=0
f=open("NEW_Avenger.txt","r")
for line in f:
    num_lines+=1
    line1=line.strip("\n")
    num_letters+=len(line1)
    list1=line.split()
    num_words+=len(list1)
f.close()
print(num_letters)
print(num_lines)
print(num_words)
"""

"""
f=open("NEW_Avenger.txt","w")
l1=["HAWKEYE : CLINT BARTON\n","BLACK WIDOW : NATASHA ROMANOFF"]
f.writelines(l1)
f.close()
"""

"""
import os
os.remove('NEW_Avenger.txt')
print(os.path.exists("NEW_Avenger.txt"))
"""

"""
f=open("myfile.txt","r")
err=0
for line in f:                       #THIS SHOULD CALCULATE ERRORS
    line=line.strip()
    if line[0].islower()==True:   
        err=err+1                   
    for j in range(len(line)):
        if line[j]==line[j+1]==" ":
            err=err+1

print("Total number of errors:",err)


L=[] 
for line in f:                        #THIS SHOULD FIX ERRORS 
    line=line.strip()                 
    if line[0].islower()==True:   
        line[0].upper()
        k=""                    
    for j in range(len(line)):
        if line[j]==line[j+1]==" ":
                      continue
        else:
            k=k+line[j]
    k=k+'\n'
    L.append(k)
f.close()

nea=open("vitap.txt","w")
nea.writelines(L)
nea.close()        
"""

"""
def re(a,b):
    if b==0:
        return a
    else:
        return re(b,a%b)

a=int(input())
b=int(input())
print(re(a,b))        
"""

"""
L=list()
print("Keep entering the words:")
c=input()
while(c!="-"):
    L.append(c)
    c=input()
    
L1=[]
for i in L:
    if i not in L1:
        L1.append(i)
            
for k in L1:
    print(k)
"""

"""    
p=set()
o=set()
l=int(input("Enter limit for prime set:"))
l1=int(input("Enter limit for odd set:"))

for i in range(1,l+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        p.add(i)
        
for i in range(1,l1+1):
    if i%2!=0:
        o.add(i)

print(p.union(o))
print(p.intersection(o))
print(p-o)
print(p^o)        
"""

"""
def Bin(a,s):
    r=a%2
    a=a//2
    s.append(r)
    if a!=0:
        return Bin(a,s)
    else:
         s.reverse()
         return s

a1=int(input())
s=list()
print("Binary:")
k=Bin(a1,s)
for i in k:
    print(i,end='')
"""

"""
f=open("F1.txt","a")
s=input()
f.write(s)
f.close()

f1=open("F1.txt","r")
print(f1.read())
f1.close()        
"""       

"""        
tup=(1,2,4,6,-3,6)
l=list(tup)
f=1
for i in l:
    f=f*i

print(f)    
"""

























