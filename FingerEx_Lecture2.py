#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 14:32:25 2025

@author: matthewaustinlewis
"""

# Finger Exercise — Lecture 2
# Assume you are given a variable named 'number' (with a numerical value).
# Write a piece of Python code that prints out one of the following strings: 
# - "positive" if the variable is positive
# - "negative" if the variable is negative
# - "zero" if the variable is equal to zero


number = 0

if number > 0:
    print("positive")
elif number < 0:
    print("negative")
    
# All other conditions are already handled —
# I think using 'else' here would be more concise and still correct
elif number == 0:
    print("zero")
    
