def read_in_file(fpath):
    pass


def read_in_std(l):
    N = int(input())
    for _ in range(N):
        line = input().rstrip().split()
        command = line[0]

        if command == 'insert':
            l.insert(int(l[1]),int(l[2]))
        elif command == 'print':
            print(l)
        elif command == 'remove':
            l.remove(int(l[1]))
        elif command == 'append':
            l.append(int(l[1]))
        elif command == 'sort':
            l.sort()
        elif command == 'pop':
            l.pop()
        elif command == 'reverse':
            l.reverse()





if __name__  == "__main__":
    l = []
    read_in_std(l)
    
