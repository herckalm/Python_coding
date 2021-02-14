# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:05:04 2019

@author: Iraklis Kalamas
"""
# implementation of karatsuba algorithm

def karatsuba(x, y):
    n = len(str(x))
    k = int(n//2)
    if n == 1:
        return x*y
    else:
        a = x//10**k
        b = x%10**k
        c = y//10**k
        d = y%10**k
        p = a+b
        q = c+d
        p2 = karatsuba(b, d)
        p1 = karatsuba(a, c)
        p3 = karatsuba(p, q)
        return p1 * 10**n + (p3 - p1 - p2)*10**k + p2



