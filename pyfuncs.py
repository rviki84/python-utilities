#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 21:57:53 2019

@author: Vignesh
"""


"""
MAP
"""
nums = [1, 2, 3, 4, 5]
# this function will calculate square
def square_num(x): 
    return x**2

# non-pythonic approach
squares = []
for num in nums:
    squares.append(square_num(num)) 
print('Non-Pythonic Approach: ', squares)

# pythonic approach
x = map(square_num, nums)
print('Pythonic Approach: ', list(x))


"""
ZIP
"""
first = [1, 3, 8, 4, 9]
second = [2, 2, 7, 5, 8]
# Iterate over two or more list at the same time
for x, y in zip(first, second):
    print(x + y)


"""
FILTER
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Will return true if input number is even
def even(x):
    return x % 2 == 0
# non-pythonic approach
even_nums = []
for num in numbers:
    if even(num):
        even_nums.append(num)
 
print('Non-Pythonic Approach: ', even_nums)
# pythonic approach
even_n = filter(even, numbers)
print('Pythonic Approach: ', list(even_n))


"""
LIST COMPREHENSION
"""
print('\nList comprehension example:')
x = [1,2,3,4,5,6,7,8,9]
squared_cubed = [y**2 if y%2==0 else y**3 for y in x]
print(squared_cubed)


"""
ENUMERATE AND DICT. COMPREHENSION
"""
print('\nEnumerate:')
L = ['blue', 'yellow', 'orange']
for i, val in enumerate(L):
    print("index is %d and value is %s" % (i, val))
 

print('\nDictionary comprehension:')
x = [1,2,3,4,5,6,7,8,9]
dc = {k:k**2 if k%2==0 else k**3 for k in x}
print(dc)

