import math

X, N = [int(a) for a in input().split()]

max_num = int(math.sqrt(X))


def is_eql(_range, last):
    # print(_range, last)
    total = 0
    if not _range:
        return 0

    tmp = last**N
    for num in reversed(_range):
        if tmp + num**N > max_num:
            continue
        elif tmp + num**N < max_num:
            tmp += num**N
    if tmp == max_num:
        total += 1

    return total +\
        is_eql(_range[0:-1], _range[-1]) + is_eql(_range[0:-1], last)


print(is_eql([a + 1 for a in range(max_num - 1)], max_num))
