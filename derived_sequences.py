#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 10:03:58 2022

@author: nate
"""

from cached_sequence import YellowstoneLikeSequence 

import bitlib as bl
import factlib as fl
import matplotlib.pyplot as plt

import EKG
import EKWolley
import Enots
import Yellowstone
import Base2

N = 4096


def ruler(title, seq_obj : YellowstoneLikeSequence, subplot_num):
    global N
    (x, y) = seq_obj.compute_table(N)    
    x_plot = []
    y_plot = []
    for i in range(1, len(x)):
        #bl.xor_bit_arr(D[i-1], D[i])
        C = bl.int_to_bit_arr(y[i]^y[i-1])            
        C0 = C
        LSB = 1
        
        '''
        while LSB < len(C) and C[0] == 0:
            C = C[1:]
            LSB = LSB + 1
        '''
        
        LSB = len(bl.int_to_bit_arr(y[i] ^ y[i-1]))
        x_plot.append(i)
        y_plot.append(2**LSB)
        
        bits = bl.int_to_bit_arr(y[i])
        print(f"{i:5}: {LSB} => {bits}")
    
    

    S = f"{title}: {seq_obj.format}_{seq_obj.name}"    
    plt.subplot(1, 2, subplot_num)
    plt.title(S)
    plt.scatter(x_plot, y_plot, c="black", s=1, marker="o")
    
    
def exp_population(title, seq_obj : YellowstoneLikeSequence, subplot_num):
    global N
    (x, y) = seq_obj.compute_table(N)    
    x_plot = []
    y_plot = []
    
    
    S = ""
    for i in range(1, len(x)):
        #bl.xor_bit_arr(D[i-1], D[i])
        C = bl.int_to_bit_arr(y[i])
        term = sum(C)

        x_plot.append(i)
        y_plot.append(2**term)
    

    S = f"{title}: {seq_obj.format}_{seq_obj.name}"    
    plt.subplot(1, 2, subplot_num)
    plt.title(S)
    plt.scatter(x_plot, y_plot, c="black", s=1, marker="o")




from IPython import display

from PIL import Image
import numpy as np

def boolean_function(title, seq_obj : YellowstoneLikeSequence, BF):

    (x, y) = seq_obj.compute_table(N)    
    x_plot = []
    y_plot = []

    img_res = 512

    pixels = np.zeros((img_res,img_res))
    
    for pixel_y in range(0, img_res):
        for pixel_x in range(0, img_res):
            res = BF(x[pixel_x], y[pixel_y])
            
            if res == True:
                pixels[pixel_y, pixel_x] = 255
            else:
                pixels[pixel_y, pixel_x] = 0

            
        
    img = Image.fromarray(pixels)
    img.show()
    print("done")
    '''
    plt.imshow(pixels,interpolation="nearest") 
    plt.tight_layout()
    plt.show()  # display it
    '''




def kth_bit_set(x, y):
    if x & (2**y) == (2**y):
        return True
    return False
    
    
    if x & (2**y - 1) == (2**y - 1):
        return True
    return False
    
    if y & x == x:
        return True
    
    
    
    return False
    
    





'''
plt.figure()
ruler("Ruler", Enots.binary_enots, 1)
ruler("Ruler", Base2.binary_base2, 2)
'''

'''
plt.figure()
exp_population("2^(s_2(a(i)))", Enots.binary_enots, 1)
exp_population("2^(s_2(a(i)))", Base2.binary_base2, 2)
'''
#plt.figure()
#boolean_function("2^(s_2(a(i)))", Base2.binary_base2, kth_bit_set)

boolean_function("2^(s_2(a(i)))", Enots.binary_enots, kth_bit_set)


