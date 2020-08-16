import cmath as cm

def read_from_std():
    ab = input()
    bc = input()
    return [ab, bc]

def find_angle(ab, bc):
    return cm.atan(ab/bc)



if __name__ == "__main__":
    l = read_from_std()
    ab = l[0]
    bc = l[1]
    angle = find_angle(ab, bc)
    print(angle)

