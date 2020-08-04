def read_from_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    next(f)
    set_A = set(map(int, f.readline().split()))
    next(f)
    set_B = set(map(int, f.readline().split()))
    return(set_A, set_B)


def read_from_std():
    input()
    set_A = set(map(int, input().split()))
    input()
    set_B = set(map(int, input().split()))
    return(set_A, set_B)


def symm_diff(set_A, set_B):
    res = set_A.difference(set_B).union(set_B.difference(set_A))
    print(*sorted(res), sep = "\n")

if __name__ == "__main__":
    (A, B) = read_from_std()
    (A, B) = read_from_file()
    symm_diff(A,B)


