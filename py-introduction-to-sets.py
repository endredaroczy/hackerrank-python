def read_from_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    n = int(f.readline())
    heights = list(map(int, f.readline().split()))
    return (n, heights)

def average(array):
    return sum(set(array))/len(set(array))

if __name__ == '__main__':
    (n, heights) = read_from_file()
    print(average(heights))
    s = {1,2,3,4,5}