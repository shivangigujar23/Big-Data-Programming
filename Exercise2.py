# -*- coding: utf-8 -*-
"""
Created on Fri May  3 20:40:28 2019

@author: Shivangi Gujar

Coding Challenge 1 : Exercise 2

"""

def PatternMatch(S1,S2):
    
    i = 0
    j = 0
    n = len(S1)
    m = len(S2)

    if len(S1) == 0 and len(S2) == 0: 
        return True
    if ((len(S2) > 1 and S2[0] == '*') or (len(S2) > 1 and S2[0] == '.')) and  len(S1) == 0: 
        return False
    if S1 in S2:
        return True
    while (i < n):
        if (S1[i] != S2[j]): 
            return False
        if (S1[i] == S2[j]): 
            i+= 1
            j+= 1
            if (j < m and S2[j] == '.'):
                i+= 1
                j+= 1
                return True
            if (j < m and S2[j] == '*'):
                i+= 1           
                j+= 1    
                return True
            return False
