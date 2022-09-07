#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 11:56:33 2022

@author: nate
"""
"""
    The enots wolley sequence except the place values are the natural numbers
    
    In other words, the integer partitions are ordered first by the integer 
    they partition, then the lexicographical order is used to break ties. 

"""

from sympy.combinatorics.partitions import IntegerPartition as IP
from tabulate import tabulate
import bitlib as bl

cache = {1: 1, 2: 2}
found = {1: True, 2: True}



def get_candidates(prev1, prev2):
    i = 1
    while True:
        yield i


def ip_to_arr(IP):
    '''
    Convert an integer partition to an array of coefficients of 1, 2, 3, ...
    '''  
    IP_dict = IP.as_dict()
    arr = []  
    for i in range(1, max(IP_dict.keys())+1):
        if i in IP_dict:
            arr.append(IP_dict[i])
            continue 
    
        #arr.append(0)
        arr.append("")
    return arr

def gen_ips():
    '''
    Generate all integer partitions in lexicographical order
    '''
    part0 = IP([1])
    part = part0
    while True:
        yield part        
        part = part.next_lex()
        if part == part0:
            part0 = IP([1]*(part0.integer+1))
            part = part0



def ip_supp(part):
    '''
    Return the support of integer partition p as a set.
    '''
    return set(part.as_dict().keys())

cache = {1: IP([1]), 2: IP([1, 2])}
found = {IP([1]): True, IP([1, 2]): True}

def ip_enots(n):
    global cache, found
    
    if n in cache:
        return cache[n]
    
    prev1 = ip_enots(n - 1)
    supp_prev1 = ip_supp(prev1)
    prev2 = ip_enots(n - 2)
    supp_prev2 = ip_supp(prev2)
    
    G = gen_ips()
    
    while True:
        
        part = next(G)    
        if part in found: 
            continue
        
        supp_part = ip_supp(part)
        
        A = len(supp_prev1.intersection(supp_part)) > 0
        B = len(supp_prev2.intersection(supp_part)) == 0
        C = supp_part.issubset(supp_prev1) == False
    
    
        if A == True and B == True and C == True:
            found[part] = True
            cache[n] = part
            return part
            




G = gen_ips()
N = 495
rows = []
i = 1
while True:
    ip = ip_enots(i)
    S = ip_to_arr(ip)
    S = [f"{ip.integer}"] + [f"{i} ="]  + S
    i = i + 1
    rows.append(S)
    
    if i == N:
        break

num_cols = max(map(lambda r: len(r), rows))
rows.insert(0, ["Integer"] + ["i"] + [i for i in range(1, num_cols)])

output = tabulate(rows)
print(output)


with open("./text_output/natural_enots.txt","w") as fp:
    fp.write(output)






















