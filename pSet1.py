# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 16:00:41 2021

@author: aniruddh.phukan
"""

# Problem 1

s = 'hobnobobsticks'

def count_vowels(s):
    
    vowels = 'aeiou'
    count = 0
    
    for v in vowels:
        count += s.count(v)
    return(count)

print(count_vowels(s))


# Problem 2

def count_string(s):
    
    string_to_find = 'bob'
    count = 0
       
    for i in range(len(s)):
        if s[i:i+3]==string_to_find:
            count += 1
    
    return(count)
    
print(count_string(s))


# Problem 3

def longest_asc_order_string(s):
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    index = [0]*len(s)
    
    for i in range(len(s)):
        index[i] = alphabet.find(s[i])
    
    start, end = 0,1
    longest_str, cur_str = s[start:end], s[start:end]
    
    for j in range(len(s)-1):
        
       if index[j] <= index[j+1]:
            end = j+2
            cur_str = s[start:end]
            
            if len(cur_str)>len(longest_str):
                longest_str = cur_str
            
       else:
            start = j+1
            end = j+2
            
            cur_str = s[start:end]
            
        
    return('Longest substring in alphabetical order is: {}'.format(longest_str))

print(longest_asc_order_string(s))