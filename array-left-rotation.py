import math
import os
import random
import re
import sys

def read_from_std():
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    return {'n':n, 'd':d, 'a':a}

def read_from_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    nd = f.readline().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, f.readline().rstrip().split()))
    f.close()
    return {'n':n, 'd':d, 'a':a}

def left_rotation(data):
    n = data['n'] #len(a)
    d = data['d'] #left shift
    a = data['a'] #list

    rotated = []
    for i,j in enumerate(a):
        diff = i-d
        if diff < 0:
            new_index = n-abs(diff)
        else:
            new_index = diff
        rotated.insert(new_index, j)
    return rotated



if __name__ == '__main__':
    d = read_from_file()
    #d = read_from_std()
    r = left_rotation(d)
    for i in r:
        print(i, end=' ')
