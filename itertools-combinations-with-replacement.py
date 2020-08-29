import itertools as it

def read_in_from_std():
    input_list = input().rstrip().rsplit()
    word = input_list[0]
    k = int(input_list[1])
    return [word, k]

def read_in_from_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    input_list = f.readline().rstrip().rsplit()
    f.close()
    word = input_list[0]
    k = int(input_list[1])
    return [word, k]


def solution(word, k):
    for i in list(it.combinations_with_replacement(sorted(word),k)):
        print(''.join(i))


if __name__ == "__main__":
   l = read_in_from_file()
   word = l[0]
   k = l[1]
   solution(word, k)