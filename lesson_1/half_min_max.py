N = int(input())
numbers = [int(a) for a in input().split()]

total = 0

# index
last_valid = None
smallest_valid = None

# if a number has passed requirements, a following number has to be bigger than
# that one and all in between then and it would be valid on the left side.
for i, num in enumerate(numbers):
    next = True
    tmp_smallest = []
    calculated = True
    if i != N - 1:
        if last_valid is None:
            for n_num in numbers[i + 1:]:
                if not num < n_num:
                    next = False
                    calculated = False
                    break
                tmp_smallest.append(n_num)
        else:
            if num < smallest_valid[0]:
                tmp_smallest = min(numbers[i + 1:])
            else:
                next = False

    prev = True
    j = i - 1
    while j >= 0:
        # this means that a previous one was already checked
        if last_valid and j == last_valid:
            break
        if not num > numbers[j]:
            prev = False
            break
        j -= 1

    if next and prev:
        last_valid = i
        # TODO: sort and every time after remove the smaller elements
        if calculated:
            smallest_valid = tmp_smallest.sort()
        else:
            for i, val in enumerate(smallest_valid):
                # NOTE: should it be < ?
                if val >= num:
                    smallest_valid.remove(i)
                else:
                    break
        total += num
        print(last_valid, smallest_valid)

print(total)
