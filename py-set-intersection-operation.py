def read_from_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    next(f)
    set_A = set(map(int, f.readline().rstrip().rsplit()))
    next(f)
    set_B = set(map(int, f.readline().rstrip().rsplit()))
    f.close()
    return(set_A, set_B)


def read_from_std():
    set_A_size = input()
    set_A = set(map(int, input().rstrip().rsplit()))
    set_B_size = input()
    set_B = set(map(int, input().rstrip().rsplit()))
    return(set_A, set_B)


def solution(set_A, set_B):
    return len(set_A & set_B)


if __name__ == "__main__":
    (A, B) = read_from_file()
    #(A, B) = read_from_std()
    res = solution(A, B)
    print(res)