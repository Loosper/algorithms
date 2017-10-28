a, b, c = [int(a) for a in input().split()]

smaller = min(a, b)
bigger = max(a, b)

for num in range(0, int(c / bigger) + 1):
    if (c - bigger * num) % smaller == 0:
        print((c - bigger * num) // smaller + num)
        break
