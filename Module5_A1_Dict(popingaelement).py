# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 17:50:27 2020

@author: vishal
"""


sample={"one":1,"two":2,3:"three",4:"four"}
print("the present dict is",sample)
print("1.enter 1 pop a string")
print("2.enter 2 pop a int ")
i=int(input("enter the method to perform"))
if(i==1):
    n=input("Enter a str want to delete")
else:
    n=int(input("Enter a int want to delete"))
print("After poping a item ")   
sample.pop(n) 
print(sample)

