def read_in_from_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    next(f)
    working_list = list(map(int ,f.readline().split()))
    set_A = set(map(int ,f.readline().split()))
    set_B = set(map(int ,f.readline().split()))
    return (working_list, set_A, set_B)



def read_in_from_std():
    dimensions = list(map(int ,input().split()))
    working_list = list(map(int ,input().split()))
    set_A = set(map(int ,input().split()))
    set_B = set(map(int ,input().split()))
    return (working_list, set_A, set_B)



def happiness_level(A, B, L):
    s = 0
    for i in L:
        if i in A:
            s += 1
        elif i in B:
            s -= 1

    return s


if __name__ == "__main__":
    (working_list, set_A, set_B) = read_in_from_file()
    #(working_list, set_A, set_B) = read_in_from_std()
    result = happiness_level(set_A, set_B, working_list)
    print(result)

