N = int(input())

numbers = [int(a) for a in input().split()]
biggest = sorted([numbers[0], numbers[1], numbers[2]], reverse=True)

i = 3

while i < len(numbers):
    # print(numbers[i], biggest)
    if biggest[0] < numbers[i]:
        biggest.insert(0, numbers[i])
    elif biggest[0] > numbers[i] > biggest[1]:
        biggest.insert(1, numbers[i])
    elif biggest[1] > numbers[i] > biggest[2]:
        biggest.insert(2, numbers[i])

    biggest = biggest[:3]
    i += 1

# or you iterate the array 3 times, skiping the largest of the previous times

print(biggest[-1])
