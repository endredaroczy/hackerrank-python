def read_from_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    set_A = set(map(int, f.readline().rstrip().rsplit()))
    number_of_other_sets = int(f.readline().rstrip())
    sets = []
    for _ in range(number_of_other_sets):
        set_ = set(map(int, f.readline().rstrip().rsplit()))
        sets.append(set_)
    f.close()
    return {'A':set_A, 'sets': sets}


def read_from_std():
    set_A = set(map(int, input().rstrip().rsplit()))
    number_of_other_sets = int(input().rstrip())
    sets = []
    for _ in range(number_of_other_sets):
        set_ = set(map(int, input().rstrip().rsplit()))
        sets.append(set_)
    return {'A':set_A, 'sets': sets}

def check_strict_subset(set_A, sets):
    return all([set_A.intersection(s) == s for s in sets])


if __name__ == "__main__":
    d = read_from_file()
    #d = read_from_std()
    set_A = d['A']
    sets = d['sets']
    l = check_strict_subset(set_A, sets)
    print(l)
