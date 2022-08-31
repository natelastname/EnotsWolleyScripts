#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 14 12:09:12 2022

@author: nate
"""
'''
    Computes the binary Enots Wolley sequence
'''



import bitlib as bl
import re

cache = {1: 1, 2: 3}
found = {1: True, 3: True}


def enots(n):
    global cache, found
    if n in cache:
        return cache[n]
    
    A = enots(n-1)
    B = enots(n-2)
    ker_A = bl.ker_int(A)
    ker_B = bl.ker_int(B)
    
    candidate = 1
    while True:
        candidate = candidate + 1

        if candidate in found:
            continue

        ker_C = bl.ker_int(candidate)
        
        prop1 = len(ker_C.intersection(ker_A)) > 0
        prop2 = len(ker_C.intersection(ker_B)) == 0
        prop3 = len(ker_C - ker_A) > 0
        
        if prop1 and prop2 and prop3:
            cache[n] = candidate
            found[candidate] = True
            return candidate


N = 100
for i in range(1, N+1):
    term = enots(i)
    S = bl.int_to_bit_str(term)
    
    S = re.sub(r'0', ' ', S)

    lbl1 = f"a({i}) = "
    lbl2 = f"= {term}"
    print(f"{lbl1:>9}{S:<15}{lbl2}")
