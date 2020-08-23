import itertools as it

def read_in_from_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    raw_input_ = f.readline().rstrip().rsplit()
    f.close()
    word = raw_input_[0]
    k = int(raw_input_[1])
    return (word, k)


def read_in_from_std():
    raw_input_ = input().rstrip().rsplit()
    word = raw_input_[0]
    k = int(raw_input_[1])
    return (word, k)


def solution(word, k):
    l = list(it.combinations(sorted(word), k))
    for s in l:
        print(''.join(s))


if __name__ == "__main__":
    (w, k) = read_in_from_file()
    for i in range(1, k + 1):
        solution(w, i)