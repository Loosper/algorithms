s = int(input())
array = [int(a) for a in input().split()]


def print_arr(array):
    for i in range(len(array)):
        print(array[i], end=' ')
    print()


for i in range(1, len(array)):
    j = i - 1
    while j >= 0:
        # print(i, j, array)
        if array[i] < array[j]:
            array[i], array[j] = array[j], array[i]
        else:
            break
        j -= 1
        i -= 1
    print_arr(array)
