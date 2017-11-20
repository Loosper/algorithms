n = int(input())
array = [int(a) for a in input().split()]


def print_arr(array):
    for i in range(len(array)):
        print(array[i], end=' ')
    print()


counter = [-1] * (max(array) + 1)

for i in range(len(array)):
    counter[array[i]] += 1

j = 0
for i in range(len(counter)):
    while counter[i] != -1:
        array[j] = i
        counter[i] -= 1
        j += 1

print_arr(array)
