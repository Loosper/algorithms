A, K, B, M, X = [int(a) for a in input().split()]


def laid(day):
    total = (day - day // K) * A + (day - day // M) * B
    # print(total)
    return total


def find(start, end, needle):
    n = (start + end) // 2

    candidate = laid(n)
    # print(candidate, n)

    if candidate >= needle and laid(n - 1) < needle:
        return n
    elif abs(start - end) <= 1:
        return -1
    elif candidate < needle:
        return find(n, end, needle)
    elif candidate > needle:
        return find(start, n, needle)


print(find(1, X + 1, X))
