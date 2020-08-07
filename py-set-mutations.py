def read_in_from_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    set_A_size = int(f.readline().rstrip())
    set_A = set(map(int, f.readline().rstrip().rsplit()))
    number_of_other_sets = int(f.readline().rstrip())
    input_data = []
    for _ in range(number_of_other_sets):
        tmp_list = f.readline().rstrip().rsplit()
        operation = tmp_list[0]
        number = int(tmp_list[1])
        set_ = set(map(int, f.readline().rstrip().rsplit()))
        input_data.append([set_, operation, number])
    return {'A' : set_A, 'data': input_data}


def read_in_from_std():
    set_A_size = int(input().rstrip())
    set_A = set(map(int, input().rstrip().rsplit()))
    number_of_other_sets = int(input().rstrip())
    input_data = []
    for _ in range(number_of_other_sets):
        tmp_list = input().rstrip().rsplit()
        operation = tmp_list[0]
        number = int(tmp_list[1])
        set_ = set(map(int, input().rstrip().rsplit()))
        input_data.append([set_, operation, number])
    return {'A' : set_A, 'data': input_data}


def set_mutations(d):
    set_A = d['A']
    data = d['data']
    for d in data:
        set_ = d[0]
        op = d[1]
        if op == 'update':
            set_A.update(set_)
        elif op == 'intersection_update':
            set_A.intersection_update(set_)
        elif op == 'difference_update':
            set_A.difference_update(set_)
        elif op == 'symmetric_difference_update':
            set_A.symmetric_difference_update(set_)
    return sum(set_A)


if __name__ == "__main__":
    d = read_in_from_file()
    #d = read_in_from_std()
    s = set_mutations(d)
    print(s)
