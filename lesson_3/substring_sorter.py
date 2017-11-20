n, l = [int(a) for a in input().split()]
string = input().strip()


def sort(start, end, array):
    for i in range(start + 1, end):
        # print(i)
        # for i in range(1, len(array)):
        j = i - 1
        while j >= start:
            # print(i, j, array)
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
            else:
                break
            j -= 1
            i -= 1
    return array


small = None

for i in range(0, n - l + 1):
    done = ''.join(sort(i, i + l, list(string)))

    small = small or done

    if done < small:
        small = done

print(small)
