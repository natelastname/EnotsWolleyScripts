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
import factlib as fl
import settings

from cached_sequence import YellowstoneLikeSequence

class EKG(YellowstoneLikeSequence):
    
    def __init__(self, supp_func, initial_vals, fmt, **kwargs):            
        self.supp_func = supp_func
        self.name = "EKG"
        self.format = fmt
        self.supp_func = supp_func
        super().__init__(f"./cache_dbs/{self.format}_{self.name}.db",
             initial_vals, 
             **kwargs)

    def _eval_seq(self, input_n):
        i = 1
        ker_A = self.supp_func(self.eval_seq(input_n-1))
    
        while True:
            if i in self.inv and self.inv[i] < input_n:
                i = i + 1
                continue
            
            ker_I = self.supp_func(i)
            
            if len(ker_I.intersection(ker_A)) > 0:
                return i

            i = i + 1

    
binary_ekg = EKG(bl.ker_int, {1: 1, 2: 2}, "binary")
primefact_ekg = EKG(fl.kernel, {1: 1, 2: 2}, "primefact")


binary_ekg.gen_tbl((1, settings.TABLE_N))
primefact_ekg.gen_tbl((1, settings.TABLE_N))