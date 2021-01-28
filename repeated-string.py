import math
import os
import random
import re
import sys

def read_from_std():
    s = input()
    n = int(input())
    return (s, n)


def write_out_to_std():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(str(result) + '\n')    
    fptr.close()


def read_from_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    s = f.readline()
    n = int(f.readline())
    f.close()
    return (s, n)


def repeatedString(s, n):
    remainder = n % len(s)
    multiplier = n // len(s)
    number_of_a = 0
    for c in s:
        if c == 'a':
            number_of_a += 1
    number_of_a *= multiplier+1
    for i in range(remainder):
        if s[i] == 'a':
            number_of_a += 1
    return number_of_a

if __name__ == '__main__':
    t = read_from_file()
    s = t[0]
    n = t[1]
    result = repeatedString(s, n)
    print(result)

