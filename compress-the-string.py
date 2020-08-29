import itertools as it

def read_from_std():
    S = input().rstrip()
    return S

def read_from_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    S = f.readline().rstrip()
    f.close()
    return S

def solution(S):
    for k, g in it.groupby(iterable = S, key= None):
        print((len((list(g))), int(k)), end = ' ')

if __name__ == "__main__":
    S = read_from_file()
    solution(S)
