N = int(input().strip())
nums = [int(a) for a in input().split()]


def print_arr(arr):
    for elem in arr:
        print(elem, end=' ')
    print()


def sort(start, end, arr):
    if end - start == 0:
        # you don't print here, becaue no merging occurs
        return [arr[start]]

    mid = (start + end) // 2
    first = sort(start, mid, arr)
    second = sort(mid + 1, end, arr)
    i = j = 0
    k = start

    # ok, i saw this on wikipedia becuase i got stuck
    # you know, this takes care of the two size swap
    for k in range(start, end + 1):
        if i < len(first) and (j >= len(second) or first[i] < second[j]):
            arr[k] = first[i]
            i += 1
        else:
            arr[k] = second[j]
            j += 1

    print_arr(arr)

    return arr[start: end + 1]


sort(0, N - 1, nums)
