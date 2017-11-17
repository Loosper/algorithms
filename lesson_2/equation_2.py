c = float(input())


def formula(n):
    return n ** 1.3 + 3 * n ** 0.7 + 9 * n ** 0.3


def find(start, end, needle):
    n = (start + end) / 2
    candidate = formula(n)

    if abs(candidate - needle) <= 10 ** -6:
        return n
    # this imght be wrong
    # elif abs(start - end) <= 1:
    #     return -1
    elif candidate < needle:
        return find(n, end, needle)
    elif candidate > needle:
        return find(start, n, needle)


start = 0
end = 10

while(True):
    # print(formula(end))
    if c < formula(end):
        break
    start = end
    end = end * 2

print(find(start, end, c))
