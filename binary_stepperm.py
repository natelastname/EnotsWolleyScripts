#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 11:43:50 2022

@author: nate
"""
'''
    Only numbers whose Hamming weight differs from that of the last term by
    at most 1 are candidates.
'''

import bitlib as bl

cache = {0: 0, 1: 1}
found = {0: True, 1: True}

def stepperm(input_n):
    global cache, found
    
    if input_n in cache:
        return cache[input_n]
    
    i = 1
    ker_A = bl.ker_int(stepperm(input_n-1))
    #ker_B = bl.ker_int(stepperm(input_n-2))

    while True:
        if i in found:
            i = i + 1
            continue
        
        ker_I = bl.ker_int(i)
        
        cond_A = abs(len(ker_A) - len(ker_I)) <= 1
        
        if cond_A == True:
            cache[input_n] = i
            found[i] = True
            return i
        
        i = i + 1
        
    
from print_table import gen_files_fmt
N = 512
gen_files_fmt(stepperm, "binary", "stepperm", irange1=(1,N), write_files=True)








