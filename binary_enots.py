#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 14 12:09:12 2022

@author: nate
"""
'''
    Computes the binary Enots Wolley sequence A338833
'''



import bitlib as bl
from cached_sequence import YellowstoneLikeSequence

class binary_enots(YellowstoneLikeSequence):
    
    def __init__(self, recompute=False):
        super().__init__("./cache_dbs/binary_enots.db", {1: 1, 2: 3}, recompute=recompute)

    def _eval_seq(self, input_n):
        i = 1
        ker_A = bl.ker_int(self.eval_seq(input_n-1))
        ker_B = bl.ker_int(self.eval_seq(input_n-2))

        while True:
            if i in self.inv and self.inv[i] < input_n:
                i = i + 1
                continue
            
            ker_I = bl.ker_int(i)
            
            prop1 = len(ker_A.intersection(ker_I)) > 0
            prop2 = len(ker_B.intersection(ker_I)) == 0
            prop3 = ker_I.issubset(ker_A) == False
        
            if prop1 and prop2 and prop3:
                return i

            i = i + 1

    

from print_table import gen_tbl_fmt
b_enots = binary_enots(recompute=True)
#(x, y) = b_enots.compute_table(2000)
gen_tbl_fmt(b_enots.eval_seq, "binary", "enots", irange1=(1,250))

