#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 11:30:33 2022

@author: nate
"""

'''
    Print the integer partitions of 1, 2, ..., N in lexicographical order
'''


from sympy.combinatorics.partitions import IntegerPartition
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
    p0 = IntegerPartition([1])
    p = p0
    while True:
        yield p        
        p = p.next_lex()
        if p == p0:
            p0 = IntegerPartition([1]*(p0.integer+1))
            p = p0

G = gen_ips()

N = 250

rows = []
rows.append(["Int"] + ["i"] + [i for i in range(1, N+1)])

i = 1
while True:
    ip = next(G)
    
    S = ip_to_arr(ip)
    S = [f"[{ip.integer}]"] + [f"{i} ="]  + S   
    i = i + 1
    rows.append(S)
    
    print(ip.integer)
    if i == N:
        break
    if ip.integer == N:
        break


output = tabulate(rows)
print(output)


with open("./text_output/partitions_lex.txt","w") as fp:
    fp.write(output)














