#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 19:13:40 2022

@author: nate
"""

import factlib as fl
from cached_sequence import YellowstoneLikeSequence

class primefact_yellowstone(YellowstoneLikeSequence):
    
    def __init__(self, recompute=False):
        super().__init__("./cache_dbs/primefact_yellowstone.db", {1: 1, 2: 2, 3: 3}, recompute=recompute)
        
    
    def _eval_seq(self, input_n):
        i = 1
        print(input_n)
        ker_A = fl.kernel(self.eval_seq(input_n-1))
        ker_B = fl.kernel(self.eval_seq(input_n-2))
    
        while True:
            if i in self.inv and self.inv[i] < input_n:
                i = i + 1
                continue
            
            ker_I = fl.kernel(i)
            cond_A = len(ker_I.intersection(ker_B)) > 0
            cond_B = len(ker_I.intersection(ker_A)) == 0
            
            if cond_A == True and cond_B == True:
                return i
            
            i = i + 1


pf_ys = primefact_yellowstone(recompute=True)
#(x, y) = bys.compute_table(100000)
    
N = 250

from print_table import gen_tbl_fmt
output = gen_tbl_fmt(pf_ys.eval_seq, "primefact", "yellowstone", irange1=(1,250))
print(output)
