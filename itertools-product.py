from itertools import product

def read_in():
    A = list(map(int, input().rstrip().rsplit()))
    B = list(map(int, input().rstrip().rsplit()))
    return [A, B]

def itertools_product(A, B):
    return list(product(A, B))

if __name__ == "__main__":
    t = read_in()
    A = t[0]
    B = t[1]
    l = itertools_product(A, B)
    for t in l:
        print(t, end = " ")