N = int(input())
numbers = [int(a) for a in input().split()]

K = numbers.index(max(numbers))
total = 0

# c?
# these are indexes
i = 0
j = len(numbers) - 1
while i < K:
    if numbers[i] == numbers[j]:
        total += 1
        i += 1
        j -= 1
    elif numbers[i] < numbers[j]:
        i += 1
    elif numbers[i] > numbers[j]:
        j -= 1

print(total)
