#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumLoss function below.
def minimumLoss(numbers):
    nums = list(numbers)
    nums.sort()
    minCost = 10**10
    for i in range(1,n):
        if (nums[i]-nums[i-1] < minCost)  and (numbers.index(nums[i]) < numbers.index(nums[i-1])):
            minCost = nums[i]-nums[i-1]
    print(minCost)


if __name__ == '__main__':
    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)
