#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 18:19:04 2022

@author: nate
"""

import bitlib as bl
import factlib as fl
import settings

from cached_sequence import YellowstoneLikeSequence

class BogusEnots(YellowstoneLikeSequence):
    
    def __init__(self, supp_func, initial_vals, fmt, recompute=None):
        self.supp_func = supp_func
        self.name = "bogus_enots"
        self.format = fmt
        self.supp_func = supp_func
        super().__init__(f"./cache_dbs/{self.format}_{self.name}.db",  initial_vals, recompute=recompute)



    def skipped_obj_rks(self):
        '''
        Generates the ranks of the ith skipped number.
        
        This can be edited, and the other methods will cope.
        '''
        term_no = 0
        while True:
            term_no += 1
            yield 2**(term_no)
            
        



    def unskipped_obj_rks(self):
        '''
        Generates the ranks of the unskipped numbers.
        '''
        G = self.skipped_obj_rks()
        next_skipped = next(G)
        
        term_no = 0
        
        while True:
            term_no += 1
            
            if term_no == next_skipped:
                next_skipped = next(G)
                continue
        
            yield term_no
        
        


    def is_obj_skipped(self, obj):
        ker_obj = bl.ker_int(obj)
        if min(ker_obj) + 1 == max(ker_obj):
            return False
        
        
        return True



    def get_obj_by_rank(self, rank):
        
        # Is this the rank of a skipped number?
        ker_rank = bl.ker_int(rank)
        
        
        if len(ker_rank) == 1:
             skipped_index = list(ker_rank)[0]
             
             
             # 9 has rank 8, so it is the third skipped number
             # there are 2log=6 excluded objects below 9
             
             # skipped_below_i + unskipped_below_i = i - math.floor(log_2(i))
        
            
            
            

    def rank_order(self):
        '''
        Generator for enumerating the natural numbers in order of rank.
        '''
        current_rank = 1        
        while True:            
            yield self.get_obj_by_rank(current_rank)

                
                
                

    def _eval_seq(self, input_n):
        i = 1
        ker_A = self.supp_func(self.eval_seq(input_n-1))
        ker_B = self.supp_func(self.eval_seq(input_n-2))

    
        G = self.rank_order()
        i = next(G)["obj"]

        while True:
            
            
            if i in self.inv and self.inv[i] < input_n:
                i = next(G)["obj"]
                continue
            
            ker_I = self.supp_func(i)
            
            prop1 = len(ker_A.intersection(ker_I)) > 0
            prop2 = len(ker_B.intersection(ker_I)) == 0
            prop3 = ker_I.issubset(ker_A) == False
        
            if prop1 and prop2 and prop3:
                return i

            i = next(G)["obj"]



bogus_enots = BogusEnots(bl.ker_int, {1: 3, 2: 6}, "binary")
G = bogus_enots.unskipped_obj_rks()
G = bogus_enots.rank_order()
for i in range(1, 10):
    term = next(G)
    print(f"{i}: {term}")


bogus_enots.gen_tbl((1, 10))

