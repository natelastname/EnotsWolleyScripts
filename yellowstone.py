#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 14 12:09:09 2022

@author: nate
"""
'''
    This is actually the Enots Wolley sequence, not the yellowstone sequence.

'''
import re 
import math
import primefac
import functools
import operator

G = primefac.primegen()
primes = [next(G) for i in range(0,100)]

def factor(n):
    factors_dict = {}
    factors = [x for x in primefac.primefac(n)]
    for fact in factors:
        if fact in factors_dict:
            factors_dict[fact] = factors_dict[fact] + 1 
            continue
        factors_dict[fact] = 1
        
    return factors_dict
    

def kernel(n):
    factors = [x for x in primefac.primefac(n)]
    return set(factors)

def combine_with_pad(arr):
    S = ""
    for i in arr:
        S = S + f"{i:>2}"
    return S

def int_to_fact_arr(n):
    global primes
    fact = factor(n)
    
    as_arr = [0]*len(primes)
    last_ind = 0
    for x in fact.keys():
        ind = primes.index(x)
        last_ind = max(last_ind, ind)
        as_arr[ind] = fact[x]
    
    return as_arr[0:last_ind+1]
    
def int_to_fact_string(n):
    as_arr = int_to_fact_arr(n)
    for i in range(0, len(as_arr)):
        if as_arr[i] == 0:
            as_arr[i] = "x"
    S = combine_with_pad(as_arr)    
    S = re.sub(r'x', ' ', S)

    return S


cache = {1: 1, 2: 2, 3: 6}
found = {1: True, 2: True, 6: True}


def yellowstone(n):    
    global cache, found
    if n in cache:
        return cache[n]
    
    A = yellowstone(n-1)
    B = yellowstone(n-2)
    ker_A = kernel(A)
    ker_B = kernel(B)
    
    candidate = 1
    while True:
        candidate = candidate + 1

        if candidate in found:
            continue

        ker_C = kernel(candidate)
        
        prop1 = len(ker_C.intersection(ker_A)) > 0
        prop2 = len(ker_C.intersection(ker_B)) == 0
        prop3 = len(ker_C - ker_A) > 0
        
        if prop1 and prop2 and prop3:
            cache[n] = candidate
            found[candidate] = True
            return candidate


N = 34
'''
trunc_primes = primes[0:14]
hack = functools.reduce(lambda x,y: str(x)+f"{str(y):>4}", trunc_primes, 1)
lbl = "            "
#print(f"{lbl:>8}{hack}")
for i in range(1, N+1):
    term = yellowstone(i)
    S = int_to_fact_string(term)
    
    lbl1 = f"a({i}) = "
    lbl2 = f"= {term}"
    print(f"{lbl1:>9}{S:<32}{lbl2}")
'''



to_print = []

for i in range(1, N+1):
    term = yellowstone(i)
    S = [i] + int_to_fact_arr(term)
    to_print.append(S)
    S = str(S)
    lbl1 = f"a({i}) = "
    lbl2 = f"= {term}"
    print(f"{lbl1:>9}{S:<32}{lbl2}")

  
num_primes = max([len(x) for x in to_print])
trunc_primes = [0]+primes[0:num_primes-1]

to_print = [trunc_primes] + to_print

printed = ""
def pprint(S):
    global printed
    printed = printed + S + "\n"
    print(S)
    
    

tab = "   "
pprint("\\begin{tikzpicture}[scale=0.55]")
pprint(tab +"\\begin{scope}")
pprint(f"{tab*2}\\draw (0, 0) grid ({num_primes}, {N+1});")

x = 0
y = N

body = ""
for i in range(0, len(to_print)):
    len_i = len(to_print[i])
    to_print[i] = to_print[i] + ([0]*(num_primes-len_i))
    to_print[i] = [ str(x) for x in to_print[i]]
    S ="\\setrow{"+"}{".join(to_print[i]) + "}"
    
    x = 0
    term_label = str(i+1)
    print(f"{term_label:>6}")
    
    
    
    for j in range(0, len(to_print[i])):
        elt = to_print[i][j]
        if elt == "0":
            elt = " "
            
        node_text = ""
        if i==0 or j==0:
            node_text = f"\\node[anchor=center,font=\\small] at ({x+0.5}, {y+0.5})"+"{"+str(elt)+"};"
            pprint(f"\\fill[orange!20] ({x},{y}) rectangle ({x+1},{y+1});")

        else:
            node_text = f"\\node[anchor=center] at ({x+0.5}, {y+0.5})"+"{"+str(elt)+"};"


        pprint(tab*2+node_text)
        x = x + 1
        

    #print(2*tab+S)
    
    y = y - 1
    
    #print(tab*2+S)
    
pprint(tab*2+f"\\node[anchor=center] at ({num_primes/2}, -0.5) "+"{Enots Wolley};")

    
pprint(tab+"\\end{scope}")

pprint("\\end{tikzpicture}")
  
with open('/home/nate/Documents/enots_wolley/enots.tikz', "w") as fp:
    fp.write(printed)




