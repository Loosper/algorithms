n = int(input().strip())

stack = []

for _ in range(n):
    query = [int(num) for num in input().split()]

    if query[0] == 1:
        if not stack or query[1] > stack[-1]:
            stack.append(query[1])
        else:
            stack.append(stack[-1])
    elif query[0] == 2:
        stack.pop()
    elif query[0] == 3:
        print(stack[-1])
