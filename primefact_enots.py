#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 18:07:13 2022

@author: nate
"""
'''
    Generate a table of formatted terms of the Enots Wolley sequence (A336957)
'''

import factlib as fl
from cached_sequence import YellowstoneLikeSequence

class binary_enots(YellowstoneLikeSequence):
    
    def __init__(self, recompute=False):
        super().__init__("./cache_dbs/primefact_enots.db", {1: 1, 2: 2}, recompute=recompute)

    def _eval_seq(self, input_n):
        i = 1
        ker_A = fl.kernel(self.eval_seq(input_n-1))
        ker_B = fl.kernel(self.eval_seq(input_n-2))

        while True:
            if i in self.inv and self.inv[i] < input_n:
                i = i + 1
                continue
            
            ker_I = fl.kernel(i)
            
            prop1 = len(ker_A.intersection(ker_I)) > 0
            prop2 = len(ker_B.intersection(ker_I)) == 0
            prop3 = ker_I.issubset(ker_A) == False
        
            if prop1 and prop2 and prop3:
                return i

            i = i + 1

    

from print_table import gen_tbl_fmt
b_enots = binary_enots(recompute=True)
#(x, y) = b_enots.compute_table(2000)
gen_tbl_fmt(b_enots.eval_seq, "primefact", "enots", irange1=(1,250))


