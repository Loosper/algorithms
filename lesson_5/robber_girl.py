n = int(input().strip())
zoo = [int(a) for a in input().split()]


while True:
    start = -1
    end = 0
    for i in range(0, len(zoo) - 1):
        if i % 2 != 0 and start != -1:
            continue

        if zoo[i] > zoo[i + 1]:
            if start == -1:
                start = i
            end = i + 1
        else:
            if start != -1:
                break

    if (end - start) % 2 == 0:
        end -= 1

    for i in range(start, end + 1, 2):
        zoo[i], zoo[i + 1] = zoo[i + 1], zoo[i]

    if start != -1:
        print(start + 1, end + 1)
        # print((start - end + 1) % 2 == 0)
    else:
        break
