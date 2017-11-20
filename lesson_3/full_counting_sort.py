n = int(input().strip())
lines = [input().strip().split() for _ in range(n)]

size = int(max(lines, key=lambda x: x[0])[0])
counter = [[] for _ in range(size + 1)]

length = len(lines)
for i in range(length):
    line = lines[i]
    counter[int(line[0])].append([line[1], '-' if i < length / 2 else '+'])


for index in counter:
    for elem, flag in index:
        if flag == '+':
            print(elem, end=' ')
        else:
            print(flag, end=' ')
