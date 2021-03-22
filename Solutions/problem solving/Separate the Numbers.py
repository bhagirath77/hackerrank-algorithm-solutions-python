#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
    check = True
    for i in range(1,len(s)//2+1):
        n = int(s[:i])
        if ''.join(map(str, [n+j for j in range(len(s)//i)]))[:len(s)] == s:
            print("YES "+str(n))
            check = False
            break
    if check:            
        print('NO')

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
