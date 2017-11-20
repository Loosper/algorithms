T = int(input())
array = []

for i in range(T):
    array.append(input().strip())

for element in array:
    length = len(element)
    if length % 2 != 0:
        print(-1)
        continue

    length //= 2
    s1 = element[:length]
    s2 = element[length:]
    letters = [0] * 26  # number of letters

    for let in s1:
        letters[ord(let) - 97] += 1

    for let in s2:
        letters[ord(let) - 97] -= 1

    total = 0
    for num in letters:
        total += abs(num)

    print(total // 2)
