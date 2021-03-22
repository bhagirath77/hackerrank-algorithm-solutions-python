#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stringConstruction function below.
def stringConstruction(s):
    x=list(s)
    y=set(x)
    print(len(y))

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)
