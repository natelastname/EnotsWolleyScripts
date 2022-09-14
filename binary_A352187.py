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
from cached_sequence import YellowstoneLikeSequence

class binary_EKWolley(YellowstoneLikeSequence):
    
    def __init__(self, recompute=False):
        super().__init__("./cache_dbs/binary_EKWolley.db", {0: 0, 1: 1}, recompute=recompute)

    def _eval_seq(self, input_n):
        i = 1
        ker_A = bl.ker_int(self.eval_seq(input_n-1))
        ker_B = bl.ker_int(self.eval_seq(input_n-2))
    
        while True:
            if i in self.inv and self.inv[i] < input_n:
                i = i + 1
                continue
            
            ker_I = bl.ker_int(i)
            cond_A = len(ker_I.intersection(ker_A)) > 0
            cond_B = len(ker_I.intersection(ker_B)) == 0
            
            if ker_A.issubset(ker_B):
                cond_B = True
            
            if cond_A == True and cond_B == True:
                return i
            
            i = i + 1

    

from print_table import gen_tbl_fmt
bEKW = binary_EKWolley(recompute=False)

(x, y) = bEKW.compute_table(2000)
gen_tbl_fmt(bEKW.eval_seq, "binary", "EKWolley", irange1=(0,250))

    