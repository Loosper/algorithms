n = int(input().strip())
m = int(input().strip())
grid = []

for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)


def getBiggestRegion(grid):
    visited = [[0 for _ in range(m)] for _ in range(n)]

    def dfs(x, y):
        signs = [-1, 0, 1]
        total = 0

        for i in signs:
            new_x = x + i
            if not (0 <= new_x < len(grid)):
                continue
            for j in signs:
                new_y = y + j
                if not (0 <= new_y < len(grid[0])):
                    continue

                if visited[new_x][new_y] == 0 and grid[new_x][new_y] == 1:
                    visited[new_x][new_y] = 1
                    total += dfs(new_x, new_y) + 1
        return total

    patch = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and grid[i][j] == 1:
                visited[i][j] = 1
                patch = max(patch, dfs(i, j) + 1)

    return patch


print(getBiggestRegion(grid))
