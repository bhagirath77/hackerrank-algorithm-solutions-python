#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    z=0
    for i in range(len(s)-1):
        if(s[i]=='A'):
            if(s[i+1]=='A'):
                z+=1
        else:
            if(s[i+1]=='B'):
                z+=1
    print(z)


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)
