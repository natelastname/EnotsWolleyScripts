#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 10:14:26 2022

@author: nate
"""

'''
If RECOMPUTE_MODE is set to True, the class YellowstoneLikeSequence will not 
load any previously computed terms from an SQLite database to memory. Instead,
it will only cache terms in a dictionary stored in RAM. Thus, this should be 
enabled when experimenting with new sequences or changing sequence definitions.
When doing computations where you want a very large amount of terms (e.g., 
generating a plot) this should be disabled.

This settings is overriden by passing True or False to the argument "recompute"
of YellowstoneLikeSequence.

'''
RECOMPUTE_MODE=True


'''
How many terms to include in the tables written to ./text_output/.
'''
TABLE_N=250

