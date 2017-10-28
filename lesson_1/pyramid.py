def get_side(columns):
    current = 0
    total = 0
    for i, col in enumerate(columns):
        if i == 0:
            current = col
            total += current
            continue

        if col >= columns[i - 1] and col >= current:
            total += col
            current = col
        else:
            total += current

    return total


N = int(input())
columns = [int(a) for a in input().split()]

total = 0
peak = columns.index(max(columns))

print(
    # peak, len(columns) - peak - 1
    get_side(columns[:peak]) +
    get_side(list(reversed(columns[peak:]))),
)
