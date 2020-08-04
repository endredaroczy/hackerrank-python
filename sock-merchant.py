def sockMerchant(n, ar):
    socks_color_list = [0] * max(ar)
    for i in ar:
        socks_color_list[i - 1] = socks_color_list[i - 1] + 1

    num_of_pairs = 0
    for i in socks_color_list:
        if i == 0:
            continue

        if i % 2 == 0:
            num_of_pairs = num_of_pairs + i / 2
        elif i > 1:
            num_of_pairs = num_of_pairs + (i-1) / 2

    return int(num_of_pairs)


if __name__ == '__main__':
    res = sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
    print(res)