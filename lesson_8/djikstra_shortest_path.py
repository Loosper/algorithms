import math


def get_line():
    return [int(a) for a in input().split()]


tests = int(input().strip())

for _ in range(tests):
    n_nodes, edges = get_line()

    nodes = [[] for a in range(n_nodes + 1)]

    for _ in range(edges):
        x, y, r = get_line()
        nodes[x].append(tuple([y, r]))
        nodes[y].append(tuple([x, r]))

    current = int(input().strip())

    distances = [math.inf for _ in range(n_nodes + 1)]
    distances[current] = 0

    visited = [False for _ in range(n_nodes + 1)]

    # print('edges:', nodes)
    while True:
        # print('unvisited', unvisited, 'current:', current)
        # print('current:', current, 'value:', distances[current])

        for other, dist in nodes[current]:
            new_dist = distances[current] + dist

            if new_dist < distances[other]:
                distances[other] = new_dist

        visited[current] = True
        current = 0

        for i in range(1, len(visited)):
            if not visited[i] and distances[i] < distances[current]:
                current = i

        if distances[current] == math.inf:
            break

        # print('distances:', distances[1:], 'smallest:', current)

    # lul slicing is very slow, what did you expect?
    # print(*[
    #     dist if dist != math.inf else -1
    #     for dist in distances[1:] if dist != 0
    # ])
    for i in range(1, len(distances)):
        if distances[i] == 0:
            continue
        print(distances[i] if distances[i] != math.inf else -1, end=' ')
    print()
