#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    for i in range(1,n):
        fizz = i % 3 == 0
        buzz = i % 5 == 0
        
        if fizz and buzz:
            print("FizzBuzz")
        elif fizz:
            print("Fizz")
        elif buzz:
            print("Buzz")
        else:
            print(i)
        

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
