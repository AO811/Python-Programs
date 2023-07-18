# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 12:12:51 2022

@author: Abhik
"""

yay=["Tony Stark",4,True,5.3,"Steve Rogers"]
print(yay)
print(yay[1:4])
print()

Avengers=["Iron Man","Captain Amwerica","Thor","Hulk","Black Widow","Hawkeye"]
print(Avengers)
Avengers.append("Ant Man")
print(Avengers)
Avengers.insert(3, "Falcon")
print(Avengers)
Avengers.remove("Ant Man")
print(Avengers)
Avengers.clear()
print(Avengers)
Avengers=["Captain Marvel","Hulk","Thor","Shang Chi","Moonknight","Ms.Marvel"]
print(Avengers)
Avengers.pop()
print(Avengers)
Avengers.pop(3)
print(Avengers)
print(Avengers.index("Thor"))
print(Avengers.count("Hulk"))
Avengers.sort()
print(Avengers)
Avengers.reverse()
print(Avengers)
New_Avengers=Avengers.copy()
print(New_Avengers)
New_Avengers.extend("IronHeart")
print(New_Avengers)
print(sorted(New_Avengers))
