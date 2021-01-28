import os
import sys


def pageCount(n, p):
    return 0


if __name__ == '__main__':
    f = open('input_file.txt')
    n = int(f.readline())
    p = int(f.readline())
    result = pageCount(n, p)
    print(str(result) + '\n')
    f.close()
