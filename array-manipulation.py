import math
import os
import random
import re
import sys

def read_from_std():
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    return {'n': n, 'queries': queries}


def write_to_std(result):
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(str(result) + '\n')
    fptr.close()


def read_from_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    nm = f.readline().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, f.readline().rstrip().split())))
    f.close()
    return {'m':m ,'n': n, 'queries': queries}

def not_my_solution():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    nm = f.readline().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, f.readline().rstrip().split())))
    f.close()
    
    array = [0] * (n + 1)
    for query in queries:
        a = query[0] - 1
        b = query[1]
        k = query[2]
        array[a] += k
        array[b] -= k
    
    max_value = 0
    running_sum = 0
    for i in array:
        running_sum += i
        if running_sum > max_value:
            max_value = running_sum
            
    return max_value

def my_write_to_std(result):
    print(result)

def arrayManipulation_slow(n, queries):
    l = [0]*n
    for q in queries:
        l[q[0]-1:q[1]] = map(lambda x: x+q[2], l[q[0]-1:q[1]])
    return max(l)

def arrayManipulation_fast(m, n, queries):
     return 0


        
if __name__ == '__main__':
    d = read_from_file()
    m = d['m']
    n = d['n']
    q = d['queries']
    result_fast = arrayManipulation_fast(m, n, q)
    result_slow = arrayManipulation_slow(n, q)
    not_my_result = not_my_solution()
    print(result_slow)
    print(result_fast)
    print(not_my_result)


