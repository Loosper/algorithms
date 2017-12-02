n = int(input().strip())

strings = []
for _ in range(n):
    strings.append([input().strip(), input().strip()])

for str1, str2 in strings:
    if len(set(str1).intersection(set(str2))) < 1:
        print('NO')
    else:
        print('YES')
