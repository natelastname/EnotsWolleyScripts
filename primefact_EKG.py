#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 08:45:28 2022

@author: nate
"""


import factlib as fl
from cached_sequence import YellowstoneLikeSequence

class primefact_EKG(YellowstoneLikeSequence):
    
    def __init__(self, recompute=False):
        super().__init__("./cache_dbs/primefact_EKG.db", {1: 1, 2:2}, recompute=recompute)

    def _eval_seq(self, input_n):
        i = 1
        ker_A = fl.kernel(self.eval_seq(input_n-1))
    
        while True:
            if i in self.inv and self.inv[i] < input_n:
                i = i + 1
                continue
            
            ker_I = fl.kernel(i)
            
            if len(ker_I.intersection(ker_A)) > 0:
                return i

            i = i + 1

    

from print_table import gen_tbl_fmt
pf_EKG = primefact_EKG(recompute=True)

#(x, y) = pf_EKG.compute_table(2000)
gen_tbl_fmt(pf_EKG.eval_seq, "primefact", "EKG", irange1=(1,250))
















