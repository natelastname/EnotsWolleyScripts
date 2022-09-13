#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 09:11:33 2022

@author: nate
"""

'''
Compute A352200, the binary version of sequence A352187 and print the results
as a human-readable table.
'''
import bitlib as bl



cache = {0: 0, 1: 1}
found = {0: True, 1: True}

def binary_EKWolley(input_n):
    global cache, found
    
    if input_n in cache:
        return cache[input_n]
    
    i = 1
    ker_A = bl.ker_int(binary_EKWolley(input_n-1))
    ker_B = bl.ker_int(binary_EKWolley(input_n-2))

    while True:
        if i in found:
            i = i + 1
            continue
        
        ker_I = bl.ker_int(i)
        cond_A = len(ker_I.intersection(ker_A)) > 0
        cond_B = len(ker_I.intersection(ker_B)) == 0
        
        if ker_A.issubset(ker_B):
            cond_B = True
        
        if cond_A == True and cond_B == True:
            cache[input_n] = i
            found[i] = True
            return i
        
        i = i + 1
        
    
from print_table import gen_files_fmt
N = 250
gen_files_fmt(binary_EKWolley, "binary", "A352187", irange1=(1,N))

    