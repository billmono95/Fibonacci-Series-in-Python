# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 09:13:55 2020

@author: Bill
"""

#ritorna tutta la sequenza
def fibonacci(n):
    l = 1       
    r = 0
    copi = []
    copi.append(0)
    
    for i in range(n-1):
        x = r
        r = r+l
        l = x
        copi.append(r)
        
    return copi     
        


#ritorna il numero maggiore della sequenza
def getNthFib(n):
    l = 1       
    r = 0
    copi = []
    copi.append(0)
    
    for i in range(n-1):
        x = r
        r = r+l
        l = x
        copi.append(r)
        copi.reverse()
        
    return copi[0]   

y = getNthFib(6)
z = fibonacci(6)
print (z) 
print(y)



