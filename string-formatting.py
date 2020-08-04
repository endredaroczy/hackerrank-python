#Given an integer n, print the following values for each integer i from 1 to n:
#Decimal return 1
#Octal oct(int)
#Hexadecimal (capitalized) hex()
#Binary

def string_formatting(n):
    for i in range(n):
        text = "{0} {0:o} {0:X} {0:b}".format(i, width = bin(n))
        print(text)

if __name__ == "__main__":
    n = 10
    string_formatting(n)