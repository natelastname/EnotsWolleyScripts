#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 13:08:41 2022

@author: nate
"""

from binary_A352187 import binary_EKWolley
from binary_EKG import binary_EKG
from binary_enots import binary_enots
from binary_yellowstone import binary_yellowstone
from primefact_EKG import primefact_EKG
from primefact_A352187 import primefact_EKWolley
from primefact_enots import primefact_enots
from primefact_yellowstone import primefact_yellowstone

import bitlib as bl
import factlib as fl

from progbar import Progbar
print_interval = 2.0

import matplotlib.pyplot as plt



print("computing terms...")
x = []
y1 = []
y2 = []
N = 5000

prog = Progbar(target=N)
for i in range(1,N):    
    prog.update(i+1)
    x.append(i)   
    term = 0
    #term = binary_enots(i)   
    resid = term - i   
    term_pop = len(bl.ker_int(term))
    
    term = binary_yellowstone(i)   
    y1.append(term-i)
    #term = primefact_enots(i)   
    y2.append(term)


    
print("Generating plot...")

#plt.cla()
plt.scatter(x, y1, c="black", s=4, marker="+")
#plt.scatter(x, y2, c="red", s=1, marker="+")
plt.show()
print("Done.")
#plot_fn_scatter(stepperm)
#print(S)


