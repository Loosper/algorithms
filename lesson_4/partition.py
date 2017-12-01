N = int(input().strip())
nums = [int(a) for a in input().split()]


def print_arr(arr):
    for elem in arr:
        print(elem, end=' ')
    # print(end=' ')


left = []
right = []
eql = []

for elem in nums:
    if elem < nums[0]:
        left.append(elem)
    elif elem < nums[0]:
        right.append(elem)
    else:
        eql.append(elem)

print_arr(left)
print_arr(eql)
print_arr(right)
