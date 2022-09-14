#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 19:47:19 2022

@author: nate
"""
'''
    Compute the sequence A352187 and generate a formatted table.
'''




import factlib as fl
from cached_sequence import YellowstoneLikeSequence

class primefact_EKWolley(YellowstoneLikeSequence):
    
    def __init__(self, recompute=False):
        super().__init__("./cache_dbs/primefact_EKWolley.db", {1: 1, 2: 2}, recompute=recompute)

    def _eval_seq(self, input_n):
        i = 1
        ker_A = fl.kernel(self.eval_seq(input_n-1))
        ker_B = fl.kernel(self.eval_seq(input_n-2))
    
        while True:
            if i in self.inv and self.inv[i] < input_n:
                i = i + 1
                continue
            
            ker_I = fl.kernel(i)
            cond_A = len(ker_I.intersection(ker_A)) > 0
            cond_B = len(ker_I.intersection(ker_B)) == 0
            
            if ker_A.issubset(ker_B):
                cond_B = True
            
            if cond_A == True and cond_B == True:
                return i
            
            i = i + 1

1
from print_table import gen_tbl_fmt
pf_EKW = primefact_EKWolley(recompute=True)
#(x, y) = pf_EKW.compute_table(2000)
gen_tbl_fmt(pf_EKW.eval_seq, "primefact", "EKWolley", irange1=(1,250))

    








import sys
sys.exit(0)


import factlib as fl
from print_table import compute_tbl_fmt



cache = {1: 1, 2: 2}
found = {1: True, 2: True}

def primefact_EKWolley(input_n):
    global cache, found
    
    if input_n in cache:
        return cache[input_n]
    
    i = 1
    ker_A = fl.kernel(primefact_EKWolley(input_n-1))
    ker_B = fl.kernel(primefact_EKWolley(input_n-2))


    while True:
        if i in found:
            i = i + 1
            continue
        
        ker_I = fl.kernel(i)
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
gen_files_fmt(primefact_EKWolley, "primefact", "A352187", irange1=(1, N))
    









    