# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 20:20:17 2020

@author: vishal
"""


def Merge(dict1, dict2): 
    return(dict2.update(dict1)) 
      

dict1 = {'a': 10, 'b': 8} 
dict2 = {'d': 6, 'c': 4} 
  
 
print(Merge(dict1, dict2)) 
   
print(dict2) 