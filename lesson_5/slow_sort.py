n = int(input().strip())

if n <= 2:
    print(-1)
else:
    for num in range(n, 0, -1):
        print(num, end=' ')
    print()
