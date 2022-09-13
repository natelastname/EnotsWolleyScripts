#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 08:45:28 2022

@author: nate
"""
import factlib as fl

cache = {1: 1, 2: 2}
found = {1: True, 2: True}

def primefact_EKG(input_n):
    global cache, found
    
    if input_n in cache:
        return cache[input_n]
    
    i = 3
    ker_A = fl.kernel(primefact_EKG(input_n - 1))
    while True:
        if i in found:
            i = i + 1
            continue
        
        ker_B = fl.kernel(i)
        
        if len(ker_A.intersection(ker_B)) > 0:
            found[i] = True
            cache[input_n] = i
            return i
        
        i = i + 1
    

from print_table import gen_files_fmt
N = 250
gen_files_fmt(primefact_EKG, "primefact", "EKG", irange1=(1, N))


















