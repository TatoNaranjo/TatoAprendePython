"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.
Given a full name, your task is to capitalize the name appropriately.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s[0].upper()
    for x in s.split():
       s= s.replace(x, x.capitalize())

    return s

if __name__ == '__main__':

    s = input()
    result = solve(s)

    print(result + '\n')


