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
import factlib as fl
import settings

from cached_sequence import YellowstoneLikeSequence

class EKWolley(YellowstoneLikeSequence):
    
    def __init__(self, supp_func, initial_vals, fmt, recompute=None):
        self.supp_func = supp_func
        self.name = "EKWolley"
        self.format = fmt
        self.supp_func = supp_func
        super().__init__(f"./cache_dbs/{self.format}_{self.name}.db",
             initial_vals, 
             recompute=recompute)

    def _eval_seq(self, input_n):
        i = 1
        ker_A = self.supp_func(self.eval_seq(input_n-1))
        ker_B = self.supp_func(self.eval_seq(input_n-2))
    
        while True:
            if i in self.inv and self.inv[i] < input_n:
                i = i + 1
                continue
            
            ker_I = self.supp_func(i)
            cond_A = len(ker_I.intersection(ker_A)) > 0
            cond_B = len(ker_I.intersection(ker_B)) == 0
            
            if ker_A.issubset(ker_B):
                cond_B = True
            
            if cond_A == True and cond_B == True:
                return i
            
            i = i + 1

    
binary_ekw = EKWolley(bl.ker_int, {1: 0, 2: 1}, "binary")
primefact_ekw = EKWolley(fl.kernel, {1: 1, 2: 2}, "primefact")


binary_ekw.gen_tbl((1, settings.TABLE_N))
primefact_ekw.gen_tbl((1, settings.TABLE_N))

