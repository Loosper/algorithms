N, K = [int(a) for a in input().split()]


# i feel like this is good enough
def find(start, end, needle):
    n = (start + end) // 2
    candidate = int(n ** 1.3 + 3 * n ** 0.7 + 9 * n ** 0.3)

    if candidate == needle:
        return n
    # this imght be wrong
    elif abs(start - end) <= 1:
        return -1
    elif candidate < needle:
        return find(n, end, needle)
    elif candidate > needle:
        return find(start, n, needle)


print(find(0, N, K))
