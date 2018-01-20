k, n = [int(_) for _ in input().split()]

stack = [k]

triplet = 0
while len(stack) < n:
    for add in [0, 3, 5]:
        stack.append(stack[triplet] * 2 + add)
    triplet += 1

print(stack[n - 1])
