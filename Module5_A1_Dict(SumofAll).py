# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 18:00:22 2020

@author: vishal
"""


def returnSum(myDict): 
      
    sum = 0
    for i in myDict: 
        sum = sum + myDict[i] 
      
    return sum
  

dict = {'a': 100, 'b':200, 'c':300} 
print("Sum :", returnSum(dict)) 
