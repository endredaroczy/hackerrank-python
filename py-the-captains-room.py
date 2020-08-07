def read_in_from_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    k = int(f.readline().rstrip())
    list_of_rooms =  list(map(int, f.readline().rstrip().rsplit()))
    f.close()
    return (k, list_of_rooms)

def read_in_from_std():
    k = int(input().rstrip())
    list_of_rooms =  list(map(int, input().rstrip().rsplit()))
    return (k, list_of_rooms)

def captains_room(k, list_of_rooms):
    d = {}
    for i in list_of_rooms:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] += 1

    for i,j in d.items():
        if j == 1:
            captains_room = i

    return captains_room
    

if __name__ == "__main__":
    (k, list_of_rooms) = read_in_from_file()
    #(k, list_of_rooms) = read_in_from_std()
    res = captains_room(k, list_of_rooms)
    print(res)