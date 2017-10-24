# i'm too lazy to do this in c.
string = input()

string = string.lower()

j = 0
valid = 1

string = [ch for ch in string if ch.isalpha()]

k = len(string) - 1

# print(string)
while j <= k:
    if string[j] != string[k]:
        valid = 0
        break
    j += 1
    k -= 1

if valid:
    print('YES')
else:
    print('NO')
