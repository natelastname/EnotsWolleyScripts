#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 08:13:29 2022

@author: nate
"""

import bitlib as bl
import factlib as fl
import settings

from cached_sequence import YellowstoneLikeSequence

class TestSeq(YellowstoneLikeSequence):
    
    def __init__(self, supp_func, initial_vals, fmt, recompute=None):
        self.supp_func = supp_func
        self.name = "testseq"
        self.format = fmt
        self.supp_func = supp_func
        super().__init__(f"./cache_dbs/{self.format}_{self.name}.db",  initial_vals, recompute=recompute)

    def _eval_seq(self, input_n):
        i = 1
        ker_A = self.supp_func(self.eval_seq(input_n-1))
        ker_B = self.supp_func(self.eval_seq(input_n-2))

        while True:
            if i in self.inv and self.inv[i] < input_n:
                i = i + 1
                continue
            
            ker_I = self.supp_func(i)
            
            prop1 = len(ker_A.intersection(ker_I)) > 0
            prop2 = len(ker_B.intersection(ker_I)) == 0
            prop3 = ker_I.issubset(ker_A) == False
        
            if prop1 and prop2 and prop3:
                return i

            i = i + 1

    
binary = TestSeq(bl.ker_int, {1: 1, 2: 3}, "binary")

binary.gen_tbl((1, settings.TABLE_N))

