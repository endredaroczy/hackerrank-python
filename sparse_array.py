
import math
import os
import random
import re
import sys


def read_from_std():
    strings_count = int(input())
    strings = []
    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)
    queries_count = int(input())
    queries = []
    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)
    return {'strings': strings, 'queries': queries}

def read_from_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    strings_count = int(f.readline())
    strings = []
    for _ in range(strings_count):
        strings_item = f.readline().rstrip()
        strings.append(strings_item)
    queries_count = int(f.readline())
    queries = []
    for _ in range(queries_count):
        queries_item = f.readline().rstrip()
        queries.append(queries_item)
    return {'strings': strings, 'queries': queries}

def write_to_std(res):
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')
    fptr.close()

def print_to_std(res):
    print('\n'.join(map(str, res)))
    print('\n')


def matchingStrings(strings, queries):
    queries_dict = {q:0 for q in queries}
    for s in strings:
        if s in queries_dict.keys():
            queries_dict[s] += 1
    
    return list(queries_dict.values())


if __name__ == '__main__':
    strings_queries = read_from_file()
    #strings_queries = read_from_std()
    strings = strings_queries['strings']
    queries = strings_queries['queries']
    res = matchingStrings(strings, queries)
    print(res)

