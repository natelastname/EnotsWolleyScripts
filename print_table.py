#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 12:38:18 2022

@author: nate
"""

from tabulate import tabulate
import bitlib as bl
import factlib as fl
import matplotlib.pyplot as plt



def compute_tbl_binary(eval_fn, i_range, fmt):
    rows = []
    start_i = i_range[0]
    end_i = i_range[1]
    for i in range(start_i, end_i + 1):
        row = []    
        term = eval_fn(i)
        lbl1 = f"a({i}) = "
        lbl2 = f"{str(term):4} = "
        S = bl.int_to_bit_arr(term)
        S = ["" if x == 0 else "1" for x in S]
        row = [lbl1, lbl2] + S    
        rows.append(row)
    
    num_cols = max(list(map(lambda x: len(x), rows))) - 1
    rows.insert(0, [" "] +[" "] + [2**i for i in range(0, num_cols)])
    output = tabulate(rows)
    return output


def compute_tbl_primefact(eval_fn, i_range, fmt):
    
    rows = []
    start_i = i_range[0]
    end_i = i_range[1]

    num_first_primes = None

    for i in range(start_i, end_i):
        term = eval_fn(i)
        fact_arr = fl.int_to_fact_arr(term)
        lbl1 = f"a({i}) = "
        lbl2 = f"{str(term):4} = "
        
        # Keep track of the index of the highest prime that is used for the 
        # purpose of generating the column labels.
        if num_first_primes == None or num_first_primes < len(fact_arr):
            num_first_primes = len(fact_arr)
        
        fact_arr = list(map(lambda x: " " if x == 0 else x, fact_arr))
        rows.append([lbl1] + [lbl2] + fact_arr)
    
    
    
    rows.insert(0, [" "] + [" "] + fl.first_n_primes(num_first_primes))

    output = tabulate(rows)
    return output




def compute_tbl_fmt(eval_fn, i_range, fmt):
    
    if fmt == "binary":
        return compute_tbl_binary(eval_fn, i_range, fmt)
    elif fmt == "primefact":
        return compute_tbl_primefact(eval_fn, i_range, fmt)
    else:
        raise Exception(f"Unknown format `{fmt}` ")




def gen_files_fmt(eval_fn, fmt, name, irange1=(1,250), irange2=(1,250), write_files=True):
    '''
        A standardized function for generating output files for each of the
        sequence.
    
        eval_fn: function that returns the ith term of the sequence
        fmt: String, the format to generate the table in
        name: String, the name of the sequence (for use in the file name)
        irange1: range to generate the formatted table in
        irange2: range to generate the list of terms in
    '''
    output1 = compute_tbl_fmt(eval_fn, irange1, fmt) 
    print(output1)
    
    
    if write_files == False:
        return
    
    
    with open(f"./text_output/{fmt}_{name}.txt","w") as fp:
        fp.write(output1+"\n")
        
        
        
    
        
        





def plot_fn_scatter(eval_fn, N):
    '''
    A small wrapper to plot an integer function with decent settings
    '''
    x = []
    y = []
    N = 1024
    for i in range(1,N):
        x.append(i)   
        term = eval_fn(i)   
        resid = term - i   
        y.append(resid)
        
        
    fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True, sharey=True)
    ax1.scatter(x, y, s=0.5)
    ax2.stem(x, y, markerfmt="None", basefmt="C0-")
    
    plt.show()




