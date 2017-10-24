N, K = input().split()
N = int(N)
K = float(K)
fence = []

try:
    while len(fence) < N:
        fence += [float(a) for a in input().split()]
except EOFError:
    pass

fence.sort()

first = 0
next = 1
max_num = 0

first = 0
next = 1
length = 1

# here i play with indexes in order to not go over already compared fields
while first < N:
    while next < N - first:
        if fence[next] - fence[first] <= K:
            length += 1
            next += 1
        else:
            break

    if length > max_num:
        max_num = length

    length -= 1
    first += 1

print(max_num)
