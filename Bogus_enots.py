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
            yield 2**(term_no+1)
            
        



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

    def rank_order(self):
        '''
        Generator for enumerating the natural numbers in order of rank.
        '''
        num_skipped = 0
        num_hit = 0
        term_i = 0
        
        
        least_unfound_rk = 1
        
        
        rank_to_int = {}
        
        G_skipped = self.skipped_obj_rks()
        G_unskipped = self.unskipped_obj_rks()
        
        
        
        
        
        while True:
            term_i = term_i + 1
            rank_i = None
            
            if len(bl.ker_int(term_i)) == 1:
                # Term has no rank because it technically isn't an object.
                continue
            
            if self.is_obj_skipped(term_i):
                # Term is unskipped.
                num_hit += 1
                rank_i = next(G_skipped)
                rank_to_int[rank_i] = {
                        "obj": term_i,
                        "rank": rank_i,
                        "skipped": True
                        }
            else:
                num_skipped += 1
                rank_i = next(G_unskipped)
                rank_to_int[rank_i] = {
                        "obj": term_i,
                        "rank": rank_i,
                        "skipped": False
                        }
                
            if least_unfound_rk in rank_to_int:
                yield rank_to_int[least_unfound_rk]
                least_unfound_rk += 1
                    
                
                
                

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
for i in range(1, 20):
    term = next(G)
    print(f"{i}: {term}")


bogus_enots.gen_tbl((1, 10))

