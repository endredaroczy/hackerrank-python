def read_in_from_std():
    number_of_test_cases = int(input().rstrip())
    test_cases = []
    for _ in range(number_of_test_cases):
        _ = input().rstrip()
        l = list(map(int, input().rstrip().rsplit()))
        test_cases.append(l)
    return test_cases

def read_in_from_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    number_of_test_cases = int(f.readline().rstrip())
    test_cases = []
    for _ in range(number_of_test_cases):
        _ = f.readline().rstrip()
        l = list(map(int, f.readline().rstrip().rsplit()))
        test_cases.append(l)
    f.close()
    return test_cases

def minimumBribes(l):
    number_of_bribes = 0
    for i in range(len(l)):
        diff = (i+1) - l[i]
        if diff > 0:
            continue
        elif abs(diff) > 2:
            return 'Too chaotic'
        else:
            number_of_bribes += abs(diff)
    return number_of_bribes




if __name__ == "__main__":
    test_cases = read_in_from_file()
    for l in test_cases:
        res = minimumBribes(l)
        print(res)
    