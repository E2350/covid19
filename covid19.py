# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 11:34:59 2020

@author: aydogdu
"""

age = (input("Are you a cigarette addict older than 75 years old? y/n : "))
chronic =(input("Do you have a severe chronic disease? y/n : "))
immune = (input("Is your immune system too weak? y/n : "))


    
if age=="y":
   age = True
else:
   age = False
if chronic =="y":
   chronic = True
else:
   chronic = False
if immune == "y":
   immune=True
else:
   immune = False
   
if age or chronic or immune:
    print("You are in riskiy group")
   
else:
    print("You are not in riskiy group")


