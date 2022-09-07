#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 10:26:17 2022

@author: nate
"""
import bitlib as bl
from print_table import compute_tbl_fmt


cache = {1: 1}
found = {1: True}

def binary_EKG(input_n):
    global cache, found
    
    if input_n in cache:
        return cache[input_n]
    
    i = 1
    ker_A = bl.ker_int(binary_EKG(input_n-1))

    while True:
        if i in found:
            i = i + 1
            continue
        
        ker_B = bl.ker_int(i)
        
        if len(ker_A.intersection(ker_B)) > 0:
            found[i] = True
            cache[input_n] = i
            return i
        
        i = i + 1


N = 257

output = compute_tbl_fmt(binary_EKG, (1, N), "binary") 
print(output)
with open("./text_output/binary_EKG.txt","w") as fp:
    fp.write(output)

    

    
    
    