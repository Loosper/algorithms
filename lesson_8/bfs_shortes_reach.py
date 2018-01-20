from queue import Queue


q = int(input().strip())
for _ in range(q):
    n, m = [int(a) for a in input().strip().split()]
    nodes = [[] for _ in range(n)]

    for _ in range(m):
        x, y = [int(a) for a in input().split()]
        nodes[x - 1].append(y - 1)
        nodes[y - 1].append(x - 1)

    s = int(input().strip()) - 1

    def bfs(node):
        distances = [-1 for _ in range(n)]
        queue = Queue()

        queue.put(node)
        # distances plays as visited
        distances[node] = 0

        while not queue.empty():
            cur_node = queue.get()
            for child in nodes[cur_node]:
                if distances[child] == -1:
                    distances[child] = distances[cur_node] + 6
                    queue.put(child)

        return distances

    print(*[a for a in bfs(s) if a != 0])
