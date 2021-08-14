#!/bin/python3

from io import StringIO
import math
import os
import random
import re
import sys

#
# Complete the 'questionableDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY transactions
#  2. INTEGER threshold
#

def sample_probability(n):
    benfords_law_dist = dict([(x, math.log10(1 + 1/x)) for x in [x for x in range(1, 10)]])
    return dict([(x, n * y) for x, y in benfords_law_dist.items()])

def non_zero_digit_counter(transactions):
    digit_counter = dict([(x + 1, 0) for x in range(9)])
    first_nonzero_digit = [int(str(x)[:1]) for x in transactions if x > 0]
    for x in first_nonzero_digit:
        digit_counter[x] = digit_counter[x] + 1
    return digit_counter

def questionableDigit(transactions, threshold):
    sample_prob = sample_probability(len(transactions))
    digit_counter = non_zero_digit_counter(transactions)
    actual_ratio = [(x, y/sample_prob[x]) for x, y in digit_counter.items()]
    compare_to_treshold = [x for x, y in actual_ratio if (y < (1 / threshold) or y > threshold)]
    print(compare_to_treshold)
    return -1 if len(compare_to_treshold) == 0 else min(compare_to_treshold)

if __name__ == '__main__':

    txtns = "987 234 1234 234873487 876 234562 17 7575734 5555 4210 678234 3999 8123"
    tresh = "3"
    transactions = list(map(int, txtns.rstrip().split()))
    threshold = int(tresh.strip())

    print (questionableDigit(transactions, threshold))
