import math
import os
import random
import re
import sys

def read_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    first_multiple_input = f.readline().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    queries = []
    for _ in range(q):
        queries.append(list(map(int, f.readline().rstrip().split())))

    return (n, queries)


def read_std_in():
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    return (n, queries)

def write_std_out(result):

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()


def dynamicArray(n, queries):
    last_answer = 0
    res = []
    d = {k:[] for k in range(n)}
    for q in queries:
        if q[0] == 1:
            index = (q[1]^last_answer) % n
            d[index].append(q[2])
        else:
            index = (q[1]^last_answer) % n
            last_answer = d[index][q[2] % len(d[index])]
            res.append(last_answer)
    return res


if __name__ == '__main__':

    #input_data = read_std_in()
    input_data = read_file()
    n = input_data[0]
    queries = input_data[1]
    result = dynamicArray(n, queries)
    print('\n'.join(map(str, result)))
    #write_std_out(result)