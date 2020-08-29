import itertools as it

def read_from_std():
    _ = int(input())
    letter_list = input().rstrip().rsplit()
    K = int(input())
    return {'letter_list':letter_list, 'K':K}

def read_from_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    _ = int(f.readline())
    letter_list = f.readline().rstrip().rsplit()
    K = int(f.readline())
    f.close()
    return {'letter_list':letter_list, 'K':K}

def solution(l, K):
    pass

if __name__ == "__main__":
    pass

