import cmath as cm


def read_from_std():
   return complex(input())


def convert(z: complex):
    print(abs(z))
    print(cm.phase(z))


if __name__ == "__main__":
    z = read_from_std()
    convert(z)

