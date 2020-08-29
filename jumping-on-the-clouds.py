import math
import os
import random
import re
import sys

def read_in_from_std():
    _ = int(input())
    cloudes = list(map(int, input().rstrip().rsplit()))
    return cloudes

def write_out_to_std(result):
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(str(result) + '\n')
    fptr.close()

def read_in_from_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    _ = int(f.readline().rstrip())
    cloudes = list(map(int, f.readline().rstrip().rsplit()))
    f.close()
    return cloudes

def jumping_on_the_clouds(cloudes):
    n = len(cloudes)
    i = 0
    jumps = 0
    while i < n:
        if i + 2 < n:
            if cloudes[i + 2] != 1:
                i += 2
                jumps += 1
            else:
                i += 1
                jumps += 1
        elif i == n-2:
            i += 1
            jumps += 1
        else:
            i += 1
    
    return jumps

if __name__ == "__main__":
    #c = read_in_from_std()
    c = read_in_from_file()
    result = jumping_on_the_clouds(c)
    print(result)
    #write_out_to_std(result)