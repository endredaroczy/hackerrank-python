def read_from_stdin():
    string = input()
    k = int(input())
    return (string, k)


def read_from_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    string = f.readline().rstrip()
    k = int(f.readline())
    return (string, k)

def merge_the_tools(string, k):
    n = len(string)
    l = list()
    segment_index = [i*k-1 for i in range((n//k)+1)]
    for i in range(0, n):
        if string[i] not in l:
            l.append(string[i])
        if i in segment_index:
            print(''.join(l))
            l.clear()
        

if __name__ == '__main__':
    (string, k) = read_from_file()
    #(string, k) = read_from_stdin()
    merge_the_tools(string, k)