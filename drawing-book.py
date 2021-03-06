import os
import sys
import math

def countFromBegining(p):
    if p % 2 == 0:
        return int(p/2)
    else:
        return int((p-1)/2)

def countFromEnd(n, p):
    if p % 2 != 0 and p != 1:
        closestEvenToActual = p-1
    else:
        closestEvenToActual = p
    
    if n % 2 != 0:
        closestEvenToEnd = n-1
    else:
        closestEvenToEnd = n
    
    return int((closestEvenToEnd-closestEvenToActual)/2)
    
def pageCount(n, p):
    fromBegining = countFromBegining(p)
    fromEnd = countFromEnd(n, p)
    if fromBegining >= fromEnd:
        return fromEnd
    else:
        return fromBegining


if __name__ == '__main__':
    f = open('input_file.txt')
    n = int(f.readline())
    p = int(f.readline())
    result = pageCount(n, p)
    print(str(result) + '\n')
    f.close()
