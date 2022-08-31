#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 09:07:41 2022

@author: nate
"""

import re 
import primefac



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


G = primefac.primegen()
primes_cache = {}
primes = []


def get_primes():
    global primes
    return primes

def find_prime_index(prime):
    global G, primes_cache

    if not primefac.isprime(prime):
        raise Exception("Argument must be a prime.")
        
    if prime in primes_cache:
        return primes_cache[prime]
    
    i = len(primes_cache.keys())
    
    while True:
        new_prime = next(G)
        primes_cache[new_prime] = i
        primes.append(new_prime)
        if new_prime == prime:
            return i
        
        i = i + 1


def int_to_fact_arr(n):
    global primes
    
    if n == 0:
        raise Exception("Can't factorize 0.")
        
    if n == 1:
        return [0]

    fact = factor(n)
    
    indices = {}
    for x in fact:
        indices[find_prime_index(x)] = fact[x]
    
    as_arr = [0]*(max(indices.keys())+1)
    
    for i in indices:
        as_arr[i] = indices[i]
        
    return as_arr
    
def int_to_fact_string(n):
    as_arr = int_to_fact_arr(n)
    for i in range(0, len(as_arr)):
        if as_arr[i] == 0:
            as_arr[i] = "x"
    S = combine_with_pad(as_arr)    
    S = re.sub(r'x', ' ', S)

    return S






assert(find_prime_index(2) == 0)
assert(find_prime_index(3) == 1)
assert(find_prime_index(5) == 2)
assert(find_prime_index(7) == 3)






