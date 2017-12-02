n = int(input().strip())
strings = []
for a in range(n):
    strings.append(input().strip())

total = 0

for string in strings:
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            total += 1
    print(total)
    total = 0
