#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    print(sum(map(str.isupper,s)) + 1)

if __name__ == '__main__':

    s = input()

    result = camelcase(s)

