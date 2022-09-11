#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 19:13:40 2022

@author: nate
"""
import factlib as fl
from print_table import compute_tbl_fmt


cache = {1: 1, 2: 2, 3: 3}
found = {1: True, 2: True, 3: True}

def primefact_yellowstone(input_n):
    global cache, found
    
    if input_n in cache:
        return cache[input_n]
    
    i = 4
    ker_A = fl.kernel(primefact_yellowstone(input_n - 1))
    ker_B = fl.kernel(primefact_yellowstone(input_n - 2))

    while True:
        if i in found:
            i = i + 1
            continue
        
        ker_i = fl.kernel(i)
        
        cond_A = len(ker_i.intersection(ker_B)) > 0
        cond_B = len(ker_i.intersection(ker_A)) == 0
        
        if cond_A == True and cond_B == True:
            found[i] = True
            cache[input_n] = i
            return i
        
        i = i + 1
        



N = 250

output = compute_tbl_fmt(primefact_yellowstone, (1, N), "primefact") 
print(output)
with open("./text_output/primefact_yellowstone.txt","w") as fp:
    fp.write(output)
