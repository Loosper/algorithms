# 1. calculate heights
# 2. remove first element from highest
# 3. repeat until equal


def height(stack):
    total = 0

    for i in range(len(stack)):
        total += stack[i]
    return total


lens = [int(_) for _ in input().split()]

stacks = [[], [], []]

for i in range(len(lens)):
    stacks[i] = [int(_) for _ in input().split()]


while True:
    heights = []
    for i in range(len(stacks)):
        heights.append(height(stacks[i]))

    # print(stacks)

    if len(set(heights)) == 1:
        print(max(heights))
        break

    for i in range(len(heights)):
        if heights[i] > min(heights):
            stacks[i].pop(0)
