#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    n_of_a = 0
    for i in s:
        if i == 'a':
            n_of_a += 1
    res = n_of_a * (n // len(s))
    for i in s[:n % len(s)]:
        if i == 'a':
            res += 1
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
