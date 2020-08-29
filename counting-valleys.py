import math
import os
import random
import re
import sys

def read_in_from_std():
    _ = int(input())
    s = input()
    return s

def write_out_to_std(result):
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(str(result) + '\n')
    fptr.close()

def read_in_from_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    _ = int(f.readline().rstrip())
    s = f.readline()
    f.close()
    return (s)

def write_out_(result):
    print(result)

def counting_valleys(s):
    rolling_sum = 0
    converted_list = [0]

    for i in s:
        if i == 'D':
            rolling_sum += -1
        else:
            rolling_sum += 1
        converted_list.append(rolling_sum)

    zero_position_index_list = []
    index = 0
    for i in converted_list:
        if i == 0:
            zero_position_index_list.append(index)
        index += 1

    result = 0
    for i in zero_position_index_list[:-1]:
        if converted_list[i+1] == -1:
            result += 1

    return result

def counting_valleys_better(s):
    seaLevel = valley = 0
    for step in s:
        if step == 'U':
            seaLevel += 1
        else:
            seaLevel -= 1
        
        if step == 'U' and seaLevel == 0:
            valley += 1
    return valley

if __name__ == "__main__":
  s = read_in_from_file()
  #s = read_in_from_std()

  #-----Algo--------
  result = counting_valleys(s)
  result_better = counting_valleys_better(s)
  #-----Algo--------

  write_out_(result)
  write_out_(result_better)
  #write_out_to_std(result)
