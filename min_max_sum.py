#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min = 1000000000
    max = 1
    total = 0
    for i in arr:
        if i < min:
            min = i
        if i > max:
            max = i
        total += i
    print(total - max, total - min)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
