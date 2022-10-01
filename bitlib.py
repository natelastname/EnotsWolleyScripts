#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 18:20:46 2022

@author: nate
"""

import math
    


def xor_bit_arr(A, B):
    C = []
    shorter = None
    longer = None
    if len(A) < len(B):
        shorter = A
        longer = B
    else:
        shorter = B 
        longer = A
    

    for i in range(0, len(longer)):

        if i < len(shorter):    
            if longer[i] == shorter[i]:
                C.append(0)
            else:
                C.append(1)
        else:
            C.append(longer[i])



    # remove trailing zeroes if any
    while C[-1] == 0:
        C = C[:-1]    
        if C == []:
            return [0]
        
    return C

        
#print(xor_bit_arr([1,1], [1,1]))
        

def ker_int(n_int):
    bits = int_to_bit_arr(n_int)
    indices = []
    for i in range(0, len(bits)):
        if bits[i] == 1:
            indices.append(i)
            
    return set(indices)

'''
    Bit array to string.
'''
def bit_arr_to_str(n_arr):
    
    if len(n_arr) == 0:
        return ""
    
    if len(n_arr) == 1:
        return str(n_arr[0])
    
    n_str = ""
    for i in range(0, len(n_arr)):
        n_str = n_str + str(n_arr[len(n_arr)-1-i])
        
    return n_str[::-1]


# If L = int_to_bit_arr(n), then L[0] is the ones digit.
def int_to_bit_arr(n_int):
    assert(n_int >= 0)
    
    if n_int <= 1:
        return [n_int]
                
    if n_int == 2: 
        return [0, 1]
    
    if n_int == 4:
        return [0, 0, 1]
    
    n_bits = math.ceil(math.log2(n_int))+1
    n_arr = []
    mask = 1
    for i in range(0, n_bits):
        if n_int & mask != 0:
            n_arr.append(1)
        else:
            n_arr.append(0)
        mask = mask + mask    
    
    if n_arr[-1] == 0:
        return n_arr[0:-1]
    return n_arr



'''
    n_arr[0] is the ones digit.    
'''
def bit_arr_to_int(n_arr):
    
    placeval = 1
    n = 0
    for i in range(0, len(n_arr)):
        b = n_arr[i]
        if b == 1:
            n += placeval
            
        placeval = placeval*2

    return n
    
def bit_str_to_int(n_arr):
    rev = list(n_arr)
    rev.reverse()
    return int(bit_arr_to_str(rev), 2)

def int_to_bit_str(n_int):
    n_arr = int_to_bit_arr(n_int)
    return bit_arr_to_str(n_arr)
        
    
    
    
    
    
    
    
    