s = int(input())
array = [int(a) for a in input().split()]

swaps = 0
for i in range(1, len(array)):
    j = i - 1
    while j >= 0:
        # print(i, j, array)
        if array[i] < array[j]:
            array[i], array[j] = array[j], array[i]
            swaps += 1
        else:
            break
        j -= 1
        i -= 1

print(swaps)
