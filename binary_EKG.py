#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 10:26:17 2022

@author: nate
"""
'''
Compute A115510, the binary EKG sequence (A064413)
'''

import bitlib as bl
from cached_sequence import YellowstoneLikeSequence

class binary_EKG(YellowstoneLikeSequence):
    
    def __init__(self, recompute=False):
        super().__init__("./cache_dbs/binary_EKG.db", {1: 1}, recompute=recompute)

    def _eval_seq(self, input_n):
        i = 1
        ker_A = bl.ker_int(self.eval_seq(input_n-1))
    
        while True:
            if i in self.inv and self.inv[i] < input_n:
                i = i + 1
                continue
            
            ker_I = bl.ker_int(i)
            
            if len(ker_I.intersection(ker_A)) > 0:
                return i

            i = i + 1

    

from print_table import gen_tbl_fmt
bEKG = binary_EKG(recompute=True)

(x, y) = bEKG.compute_table(2000)
gen_tbl_fmt(bEKG.eval_seq, "binary", "EKG", irange1=(1,250))

import sys 
sys.exit(0)
