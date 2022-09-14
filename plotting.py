#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 13:08:41 2022

@author: nate
"""

from cached_sequence import YellowstoneLikeSequence 

import bitlib as bl
import factlib as fl
import matplotlib.pyplot as plt

import EKG
import EKWolley as EKW
import Enots
import Yellowstone as YS


N = 5000

def scatter_plot(seq_obj : YellowstoneLikeSequence, i):
    global N
    S = f"{seq_obj.format}_{seq_obj.name}"
    print(f"Computing table for {S}...")
    (x, y) = seq_obj.compute_table(N)
    plt.subplot(1, 2, i)
    plt.title(S)
    plt.scatter(x, y, c="black", s=4, marker="+")


plt.figure()
scatter_plot(Enots.binary_enots, 1)
scatter_plot(Enots.primefact_enots, 2)
plt.figure()
scatter_plot(EKW.binary_ekw, 1)
scatter_plot(EKW.primefact_ekw, 2)
plt.figure()
scatter_plot(EKG.binary_ekg, 1)
scatter_plot(EKG.primefact_ekg, 2)
plt.figure()
scatter_plot(YS.binary_ys, 1)
scatter_plot(YS.primefact_ys, 2)



import sys
sys.exit(0)


