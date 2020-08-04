def read_in_from_file():
    f = open('C:\\Users\\dkendre\\source\\repos\\scripts-python\\hackerrank\\input_file.txt', 'r')
    num_of_countries = int(f.readline().rstrip())
    country_set = set()
    for _ in range(num_of_countries):
        country_set.add(f.readline().rstrip())
    return country_set

def read_in_from_std():
    num_of_countries = int(input().rstrip())
    country_set = set()
    for _ in range(num_of_countries):
        country_set.add(input().rstrip())
    return country_set


def number_of_distinct_countries(country_set):
    return len(country_set)


if __name__ == "__main__":
    country_set = read_in_from_file()
    #country_set = read_in_from_std()
    res = number_of_distinct_countries(country_set)
    print(res)
