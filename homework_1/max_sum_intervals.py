# add numbers until you have a postivie sum. Once it goes below 0, reset

# alternate solution:
# have a second list with sums up intil this point.
# Then to see the sum of a certain interval we just subtract the sum before it
# to find the biggesst sum: subtract the smallest from the biggest one
# (which is half min half max task)

N = int(input())
numbers = [int(a) for a in input().split()]
# the smallest number in the task
max_sum = 2 * int(-1e09)

total = 0
for num in numbers:
    if total < 0:
        total = 0
    # for negative intervals, we need the biggest single negative, otherwise
    # the sum would beome smaller
    total += num

    if total > max_sum:
        max_sum = total

print(max_sum)
