def read_in_from_std():
    len_set_english = int(input().rstrip())
    set_english = set(map(int, input().rstrip().split()))
    len_set_french = int(input().rstrip())
    set_french = set(map(int, input().rstrip().split()))
    return {'set_english': set_english, 'set_french' : set_french}

def read_in_from_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    len_set_english = int(f.readline().rstrip())
    set_english = set(map(int, f.readline().rstrip().split()))
    len_set_french = int(f.readline().rstrip())
    set_french = set(map(int, f.readline().rstrip().split()))
    return {'set_english': set_english, 'set_french' : set_french}


def py_set_union(dict_):
    return (len(dict_['set_english']) + len(dict_['set_french'])) - len(dict_['set_english'].intersection(dict_['set_french']))


if __name__ == "__main__":
   l = read_in_from_file() 
   #l = read_in_from_std()
   res = py_set_union(l)
   print(res)