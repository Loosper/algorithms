# sort the crashes and then you don't have to iterate every time

n = int(input().strip())
scores = [int(a) for a in input().split()]
max_score = sum(scores)
crashes = []

while True:
    crash = int(input().strip())
    crashes.append(crash)
    if crash == max_score:
        break

crashes.sort()

cur_score = scores[0]
i = 0
j = 0
total = 0

while j < len(crashes):
    if crashes[j] > cur_score:
        i += 1
        cur_score += scores[i]
    else:
        if crashes[j] != 0:
            total += i + 1
        j += 1

print(total)
