#Given an array of n numbers what is the largest possible sum of a sequance of consecutive values in the array
#Consider sub-problem of finding the maximum subarray that ends at position k
#There are two options: 
#1) The subarray only contains the element at position k
#2) The subarray consists of a subarray that ends at position k-1 followed by the element at position k
#arr = [-1, 2, 4, -3, 5, 2, -5, 2]
def read_from_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    arr = list(map(int, f.readline().split()))
    f.close()
    return arr

def max_sub_array(arr):
    best = 0
    sum = 0
    n = len(arr)
    for k in range(n):
        sum = max(arr[k], sum + arr[k])
        best = max(best, sum)
    return best

if __name__ == '__main__':
    arr = read_from_file()
    res = max_sub_array(arr)
    print(res)
