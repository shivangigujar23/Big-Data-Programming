# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 16:59:00 2019

@author: Shivangi
"""

import numpy as np

# Exercise 1
arr = np.array([0,1,2,3,4,5,6,7,8,9])
arr[1::2] = -1
print(arr)

# Exercise 2
arr = np.arange(10)
arr = arr.reshape(2,-1)
print(arr)

# Exercise 3
arr = np.array([1,2,3])
arr = np.r_[np.repeat(arr, 3), np.tile(arr, 3)]
print(arr)

# Exercise 4
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
arr = np.intersect1d(a,b)
print(arr)

# Exercise 5
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
arr = np.where(a == b)
print(arr)

# Exercise 6
arr = np.arange(9).reshape(3,3)
random_arr = np.random.randint(low=5, high=10, size=(5,3)) + np.random.random((5,3))
print(random_arr)

# Exercise 7
np.set_printoptions(threshold = 6)
arr= np.arange(15)
print(arr)

# Exercise 8
np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3
np.set_printoptions(suppress=True, precision=6)
print(rand_arr)

# Exercise 9
arr = np.arange(9).reshape(3,3)
arr = arr[:, [1,0,2]]
print(arr)

# Exercise 10
arr = np.arange(9).reshape(3,3)
arr = arr[[1,0,2], :]
print(arr)

