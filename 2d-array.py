def read_from_stdin():
    arr = []
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    for _ in range(6):
        arr.append(list(map(int, f.readline().split())))
    return arr

def hourglassSum(arr):
    glob_max = -10000000000
    for i in range(4):
        for j in range(4):
            l = [row[j:j+3] for row in arr[i:i+3]]
            l_sum = 0
            for k in range(3):
                if k == 1:
                    l_sum += l[k][1]
                else:
                    l_sum += sum(l[k])
            if glob_max < l_sum:
                glob_max = l_sum
    return glob_max


if __name__ == '__main__':
    arr = read_from_stdin()
    res = hourglassSum(arr)
    print(res)
   