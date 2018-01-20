n = int(input().strip())

pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}

openers = pairs.values()

for _ in range(n):
    helper = []
    brackets = input().strip()

    for char in brackets:
        if char in openers:
            helper.append(char)
        else:
            try:
                if pairs.get(char, None) == helper[-1]:
                    helper.pop()
                else:
                    break
            except:
                # this is an ugly hack, but it works
                helper = [1]
                break

    if len(helper) == 0:
        print('YES')
    else:
        print('NO')
