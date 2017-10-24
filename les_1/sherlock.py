def solve(nums):
    left = 0
    right = sum(nums[1:])

    for i in range(0, len(nums)):
        if i > 0:
            left += nums[i - 1]
            right -= nums[i]

        # print(left, right)
        if left == right:
            return 'YES'

    return 'NO'


# template for the solution
T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    # NOTE: map() replaces the list comprehensions you've been doing
    a = list(map(int, input().strip().split(' ')))
    result = solve(a)
    print(result)
