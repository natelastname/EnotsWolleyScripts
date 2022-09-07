#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 12:01:33 2022

@author: nate
"""

import binary_enots
import bitlib as bl

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
    term = binary_enots.enots(i)
    S = [i] + bl.int_to_bit_arr(term)
    to_print.append(S)
    S = str(S)
    lbl1 = f"a({i}) = "
    lbl2 = f"= {term}"
    print(f"{lbl1:>9}{S:<32}{lbl2}")


primes = [2**i for i in range(0, 100)]
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
pprint(f"{tab*2}\\draw[step=1cm] (0, 0) grid ({num_primes}, {N+1});")

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

            
        node_text = ""
        if i==0 or j==0:
            node_text = f"\\node[anchor=center,font=\\small] at ({x+0.5}, {y+0.5})"+"{"+str(elt)+"};"
            pprint(f"\\fill[orange!20] ({x},{y}) rectangle ({x+1},{y+1});")

        
        else:
            node_text = f"\\node[anchor=center] at ({x+0.5}, {y+0.5})"+"{"+str(elt)+"};"


        if elt != "0":
            pprint(tab*2+node_text)
        x = x + 1
        

    #print(2*tab+S)
    y = y - 1
    #print(tab*2+S)
    

pprint(tab*2+f"\\node[anchor=center] at ({num_primes/2}, -0.5) "+"{Binary Enots Wolley};")

pprint(tab+"\\end{scope}")

pprint("\\end{tikzpicture}")
  
with open('./text_output/binary_enots.tikz', "w") as fp:
    fp.write(printed)






