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
    
    Stores everything in memory until you call table_generator.commit()
    
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



class YellowstoneLikeSequence:
    '''
        Automatically stores the function and its inverse to a key value store.
        
        Beware cache invalidation. I.e., this does not behave well when you are 
        changing the implementation of the underlying function.
    '''    
    def __init__(self, filename : str, initial_vals : dict):
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

    def _eval_seq(self, input_i):
        '''
        Implement your function here.
        '''
        return -1
    
    def compute_table(self, N):
        prog = Progbar(target=N)

        x = []
        y = []
        for i in range(1, N):
            prog.update(i+1)
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
    YellowstoneLikeSequence (for testing purposes.)
    '''
    def __init__(self):
        super().__init__("./cache_dbs/nat.db", {0: 0})

    def _eval_seq(self, input_i):        
        value = self.eval_seq(input_i - 1) + 1
        return value
            
    
nat = natural_numbers()
nat.eval_seq(10)

###############################################################################

import bitlib as bl

class binary_yellowstone(YellowstoneLikeSequence):
    
    def __init__(self):
        super().__init__("./cache_dbs/binary_yellowstone.db", {0: 0, 1: 1, 2: 2})


    def _eval_seq(self, input_i):   
        A = self.eval_seq(input_i-1)
        B = self.eval_seq(input_i-2)
        ker_A = bl.ker_int(A)
        ker_B = bl.ker_int(B)
        
        candidate = 1
        while True:
            candidate = candidate + 1
    
            if candidate in self.inv:
                continue
    
            ker_candidate = bl.ker_int(candidate)
            
            prop1 = len(ker_candidate.intersection(ker_B)) > 0
            prop2 = len(ker_candidate.intersection(ker_A)) == 0
            
            if prop1 and prop2:
                return candidate
    

    
    
bys = binary_yellowstone()
bys.eval_seq(40)

bys.compute_table(100000)
    
    
    