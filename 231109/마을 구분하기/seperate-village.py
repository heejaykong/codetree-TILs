n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]


def solution(grid):
    n = len(grid)
    visited = [[False] * n for i in range(n)]
    dxs, dys = [0, 1, 0,-1], [1, 0,-1, 0]
    WALL, NOT_WALL = 0, 1
    village_count = 0
    curr_count = 0
    populations = []

    def push(x, y):
        visited[x][y] = True
    
    def in_range(x, y):
        return 0 <= x < n and 0 <= y < n
    
    def can_go(x, y):
        if not in_range(x, y):
            return False
        if visited[x][y]:
            return False
        if grid[x][y] == WALL:
            return False
        return True

    def dfs(x, y):
        nonlocal curr_count

        for dx, dy in zip(dxs, dys):
            nx, ny = dx + x, dy + y

            if can_go(nx, ny):
                curr_count += 1
                push(nx, ny)
                dfs(nx, ny)


    for i in range(n):
        for j in range(n):
            if not visited[i][j] and grid[i][j] == NOT_WALL:
                village_count += 1

                curr_count = 1
                push(i, j)
                dfs(i, j)
                populations.append(curr_count)

    populations.sort()
    
    return (village_count, populations)


# ========
ans = solution(grid)
print(ans[0])
for pop in ans[1]:
    print(pop)