# -*- coding: utf-8 -*-
"""
Created on Fri May  3 20:26:34 2019

@author: Shivangi Gujar

Coding Challenge 1 : Exercise 1

"""

def lcs(StringS1, StringS2):
     if StringS1 == '' or StringS2 == '':
             return []
     S1, S2, S1t, S2t = StringS1[0], StringS2[0], StringS1[1:], StringS2[1:]
     if S1 == S2:
             return [S1] + lcs(S1t,S2t)
     else:
             return max(lcs(StringS1,S2t), lcs(S1t,StringS2), key=len)   
