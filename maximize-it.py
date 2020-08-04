import os
import math

def read_in_file():
    f = open('C:\\Users\\dkendre\\Desktop\\input_file.txt', 'r')
    km = f.readline().rstrip().split()
    k = int(km[0])
    m = int(km[1])
    list_of_lists = []
    for _ in range(k):
        list_of_lists.append(list(map(int, f.readline().rstrip().split())))
    f.close()
    return {'input_lists': list_of_lists, 'divisor': m}


def read_in_stdin():
    km = input().rstrip().split()
    k = int(km[0])
    m = int(km[1])
    list_of_lists = []
    for _ in range(k):
        list_of_lists.append(list(map(int, input().rstrip().split())))
    return {'input_lists': list_of_lists, 'divisor': m}


def write_out_stdout(result):
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(str(result))


def maximize_it(input_lists, input_divisor):
    sum = 0
    for l in input_lists:
        minim = 1
        for j in l:
            diff = (j*j)/input_divisor - math.floor((j*j)/input_divisor)
            if diff < minim:
                minim = diff
                min_value = j*j
        sum = sum + min_value
    return sum%input_divisor


if __name__ == '__main__':
    input_data = read_in_file()
    #input_data = read_in_stdin()
    input_lists = input_data['input_lists']
    input_divisor = input_data['divisor']
    r = maximize_it(input_lists, input_divisor)
    print(r)
    # write_out_stdout(206)




