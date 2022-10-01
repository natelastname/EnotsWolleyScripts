#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 10:14:13 2022

@author: nate
"""


import bitlib as bl
import factlib as fl
import settings

from cached_sequence import YellowstoneLikeSequence

class Base2(YellowstoneLikeSequence):
    
    
    '''
        Normal base 2 numbers as a YellowStoneLikeSequence.
    '''
    def __init__(self, supp_func, initial_vals, fmt, recompute=None):
        self.supp_func = supp_func
        self.name = "base2"
        self.format = fmt
        self.supp_func = supp_func
        super().__init__(f"./cache_dbs/{self.format}_{self.name}.db",  initial_vals, recompute=recompute)

    def _eval_seq(self, input_n):
        return input_n

    
binary_base2 = Base2(bl.ker_int, {1: 1}, "binary")
primefact_base2 = Base2(fl.kernel, {1: 1}, "primefact")

binary_base2.gen_tbl((1, settings.TABLE_N))
primefact_base2.gen_tbl((1, settings.TABLE_N))



