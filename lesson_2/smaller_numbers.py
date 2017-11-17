def _input():
    return [int(a) for a in input().split()]


def find(start, end, needle, elements):
    n = (start + end) // 2
    candidate = elements[n]

    if candidate == needle:
        return n
    # this imght be wrong
    elif abs(start - end) <= 1:
        return -1
    elif candidate < needle:
        return find(n, end, needle, elements)
    elif candidate > needle:
        return find(start, n, needle, elements)


N, K = _input()
tickets = _input()
elements = _input()

tickets.sort()

for num in elements:
    print(find(0, len(tickets), num, tickets), end=' ')
