#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 18:24:54 2022

@author: nate
"""

import sqlite3
from progbar import Progbar

class table_generator:
    '''
    This class behaves as a wrapper around a deterministic integer function. 
    It saves all values to disk, and it can load an existing table from a file.
   
    Uses sqlite3 as a key-value store.
    
    Stores everything in a dict until you call table_generator.commit(), which
    writes the dict to a database.
    
    '''
    def __init__(self, filename: str, tbl_name : str = "cache"):
        self.tbl_name = tbl_name
        self.filename = filename
        self.conn = sqlite3.connect(filename)
        self.conn.execute(f"CREATE TABLE IF NOT EXISTS {self.tbl_name} (key INTEGER UNIQUE, value INTEGER)")
        # This is a meta-cache: a copy of the most recently accessed values 
        # which is not stored in disc.
        self.cache_dict = {}
        
        # Load the whole key/value store to self.cache_dict.
        items = self.conn.execute(f'SELECT * FROM {self.tbl_name}').fetchall()
        
        #print(items)
        for pair in items:
            self.cache_dict[pair[0]] = pair[1]
        
        
    def __setitem__(self, key, value):
        #self.conn.execute(f'REPLACE INTO {self.tbl_name} (key, value) VALUES (?,?)', (key, value))
        self.cache_dict[key] = value
        

    def __getitem__(self, key):
        if key in self.cache_dict:
            return self.cache_dict[key]
        
        raise KeyError(key)
        
        item = self.conn.execute(f'SELECT value FROM {self.tbl_name} WHERE key = ?', (key,)).fetchone()
        if item is None:
            raise KeyError(key)
        return item[0]
        
    def __contains__(self, key):
        return key in self.cache_dict
        #return self.conn.execute(f'SELECT 1 FROM {self.tbl_name} WHERE key = ?', (key,)).fetchone() is not None

    def commit(self):
        '''
            Save the cache to the database.
        '''
        for key in self.cache_dict:
            value = self.cache_dict[key]
            self.conn.execute(f'REPLACE INTO {self.tbl_name} (key, value) VALUES (?,?)', (key, value))

        
        self.conn.commit()

    def get_min_uncomputed(self):
        '''
        Return the minimum integer which is not yet stored.
        This is currently unused because there are more efficient ways to skip
        gaps.
        '''
        res = self.conn.execute(f"SELECT MIN(key) + 1 FROM {self.tbl_name} WHERE key + 1 NOT IN (SELECT key FROM {self.tbl_name})")
        res = res.fetchone()[0]
        
        if res == None:
            return 0
        
        return res


class YellowstoneLikeSequence:
    '''
        Automatically stores the function and its inverse to a key value store.
        
        Beware cache invalidation. I.e., this does not behave well when you are 
        changing the implementation of the underlying function.
        
        If recompute=True, it won't load from or store anything in the DB. 
        Values will still be cached in a dictionary, but you can rely on any 
        changes that you made to the implementation taking effect.
        
    '''    
    def __init__(self, filename : str, initial_vals : dict, recompute=False):
        self.recompute = recompute
        
        if self.recompute:
            self.fwd = {}
            self.inv = {}
        else:
            self.fwd = table_generator(filename, "fwd")
            self.inv = table_generator(filename, "inv")
        
        for key in initial_vals:
            val = initial_vals[key]
            self.fwd[key] = val
            self.inv[val] = key

    def commit(self):
        '''
        Write the current cache to disk.
        '''
        if self.recompute:
            return
        
        self.fwd.commit()
        self.inv.commit()


    def eval_seq(self, input_i):
        '''
        If the cache contains input_i, return the cached value.
        Otherwise, compute and store f(input_i).
        '''
        if input_i in self.fwd:
            return self.fwd[input_i]
        
        value_i = self._eval_seq(input_i) 
        self.fwd[input_i] = value_i
        self.inv[value_i] = input_i
        
        return value_i

    def check_if_candidate(self, number : int, term_num : int):
        '''
            Check if the integer "number" is a candidate for the (term_num)-th 
            term. Remember that the definition of "candidate" does not require 
            that the number be unused nor minimal; these properties are handled
            by the other parts of the class.
        '''
        pass


    def _eval_seq(self, term_no):
        '''
            Compute values of the sequence without worrying about caching.
        '''
        number = 0
        while True:
            number = number + 1
    
            if number in self.inv and self.inv[number] <= term_no:
                # skip number if it occurs previously in the sequence.
                continue
    
            if self.check_if_candidate(number, term_no) == True:
                return number
    
    def compute_table(self, N):
        '''
        Compute a (potentially large) number of values of the sequence, 
        incrementally saving computed values to disc.
        '''
        prog = Progbar(target=N)
        x = []
        y = []
        for i in range(1, N):
            prog.update(i)
            term = self.eval_seq(i)
            x.append(i)
            y.append(term)
            
            if i % 1000 == 0:
                self.commit()
            
        self.commit()
        
        return (x, y)
            
        
    
###############################################################################

class natural_numbers(YellowstoneLikeSequence):
    '''
    The natural numbers 0, 1, 2, 3, ... implemented as a 
    YellowstoneLikeSequence (for testing/example purposes.)
    '''
    def __init__(self, recompute=False):
        super().__init__("./cache_dbs/nat.db", {0: 0}, recompute=recompute)

    def _eval_seq(self, input_i):
        '''
        You can either implement the method check_if_candidate, or you can
        directly write whatever you need to do to compute the ith term here.
        '''
        value = self.eval_seq(input_i - 1) + 1
        return value
            
    
#nat = natural_numbers()
#nat.eval_seq(10)

    