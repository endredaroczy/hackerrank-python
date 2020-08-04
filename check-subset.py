
def read_in_std():
    pass

def read_in_file():
    f = open('C:\\Users\\dkendre\\Desktop\\input_file.txt', 'r')
    is_subset_list = []
    number_of_test_cases = int(f.readline())
    test_case_all = []
    for i in range(number_of_test_cases):
        test_case = {}
        size_A = int(f.readline())
        set_A = set(map(int, f.readline().split()))
        size_B = int(f.readline())
        set_B = set(map(int, f.readline().split()))
        test_case['A'] = [size_A, set_A]
        test_case['B'] = [size_B, set_B]
        test_case_all.append(test_case)
        is_subset_list.append(set_A.issubset(set_B))


#{'A': [5, {1, 2, 3, 5, 6}], 'B': [9, {1, 2, 3, 4, 5, 6, 7, 8, 9}]}

if __name__ == '__main__':
    k = read_in_file()