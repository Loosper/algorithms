N = int(input().strip())
nums = [int(a) for a in input().split()]
K = int(input().strip())


def quicksort(start, end, arr):
    if end - start <= 0:
        return
    else:
        i = start
        for j in range(start, end + 1):
            if arr[j] < arr[end]:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1

        arr[i], arr[end] = arr[end], arr[i]

        quicksort(start, i - 1, arr)
        quicksort(i + 1, end, arr)


quicksort(0, len(nums) - 1, nums)
print(nums[K - 1])
