def print_hept(hept):
    for num in reversed(hept):
        print(num, end='')
    print()


number = int(input())
heptadecimal = []
# tmp = 7
# i = 0
#
# while 1:
#     if tmp**i >= number:
#         heptadecimal.append(i - 1)
#         number -= tmp**i
#         break
#     else:
#         i += 1
#
# for power in range(i)

# while number != 0:
#     a = number % 7
#     print(a)
#     heptadecimal.append(a)
#     # number = (number - a) // 7
#     number -= a
#     number //= 7
print_hept(heptadecimal)

exit()


total = [0]
i = 0
for num in heptadecimal:
    total[i] += num
    if total[i] >= 7:
        total.append(total[i] - 7 or 1)
        total[i] -= 7
        i += 1

print_hept(total)
