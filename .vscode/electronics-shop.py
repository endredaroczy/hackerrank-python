import os
import sys

def getMoneySpent(keyboards, drives, b):
    keyboards.sort(reverse = True)
    drives.sort()
    res = -1
    for i in drives:
        for j in keyboards:
            if b >= (i+j):
                res = max(res, i+j)
    return res

if __name__ == '__main__':
    f = open('input_file.txt')

    bnm = f.readline().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, f.readline().rstrip().split()))

    drives = list(map(int, f.readline().rstrip().split()))

    moneySpent = getMoneySpent(drives, keyboards, b)

    print(str(moneySpent) + '\n')
