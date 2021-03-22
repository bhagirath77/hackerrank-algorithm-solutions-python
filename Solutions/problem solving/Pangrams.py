#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    x=list(s.lower())
    y=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    for i in y:
        if(x.count(i)==0):
            print("not pangram")
            break
    else:
        print("pangram")


if __name__ == '__main__':

    s = input()

    result = pangrams(s)

