# put first name in stack
# if it's the same as the top one, put in stack
# if it's different pop the top name
# you can also save the name in the stack
# as well as how many times it's encountered
n = int(input())
# TODO: put optimisation as in line 5
stack = []

for _ in range(n):
    name = input().strip()
    if not stack or name == stack[-1]:
        stack.append(name)
    else:
        stack.pop()

print(stack[-1])
