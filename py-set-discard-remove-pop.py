#pop, remove, discard

def read_from_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    next(f)
    set_ = set(map(int, f.readline().split()))
    number_of_commands = int(f.readline().rstrip())
    for _ in range(number_of_commands):
        line = f.readline().rstrip().split()
        if line[0] == 'pop':
            set_.pop()
        else:
            if line[0] == 'remove':
                set_.remove(int(line[1]))
            elif line[0] == 'discard':
                set_.discard(int(line[1]))
    return sum(set_)
            
if __name__ == "__main__":
    A = read_from_file()
    print(*A, sep = '\n')