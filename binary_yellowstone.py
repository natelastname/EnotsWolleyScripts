#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 19:37:30 2022

@author: nate
"""
import bitlib as bl
from cached_sequence import YellowstoneLikeSequence

class binary_yellowstone(YellowstoneLikeSequence):
    
    def __init__(self, recompute=False):
        super().__init__("./cache_dbs/binary_yellowstone.db", {0: 0, 1: 1, 2: 2}, recompute=recompute)
        
    
    def _eval_seq(self, input_n):
        i = 1
        print(input_n)
        ker_A = bl.ker_int(self.eval_seq(input_n-1))
        ker_B = bl.ker_int(self.eval_seq(input_n-2))
    
        while True:
            if i in self.inv and self.inv[i] < input_n:
                i = i + 1
                continue
            
            ker_I = bl.ker_int(i)
            cond_A = len(ker_I.intersection(ker_B)) > 0
            cond_B = len(ker_I.intersection(ker_A)) == 0
            
            if cond_A == True and cond_B == True:
                return i
            
            i = i + 1


bys = binary_yellowstone(recompute=True)
#(x, y) = bys.compute_table(100000)
    
N = 250

from print_table import gen_tbl_fmt
output = gen_tbl_fmt(bys.eval_seq, "binary", "yellowstone", irange1=(0,250))
print(output)

