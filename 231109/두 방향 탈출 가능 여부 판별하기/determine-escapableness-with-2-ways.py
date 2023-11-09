n,m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for i in range(n)]


def solution(grid):
    n = len(grid); m = len(grid[0])
    SNAKE, BLANK = 0, 1
    start_x, start_y = 0, 0
    end_x, end_y = n -1, m - 1
    POSSIBLE, IMPOSSIBLE = 1, 0

    # init
    dxs, dys = [1, 0], [0, 1]
    visited = [[False] * m for i in range(n)]
    

    def push(x, y):
        visited[x][y] = True
    
    def in_range(x, y):
        return 0 <= x < n and 0 <= y < m

    def can_go(x, y):
        if not in_range(x, y):
            return False
        if visited[x][y]:
            return False
        if grid[x][y] == SNAKE:
            return False
        return True

    def dfs(x, y):
        for dx, dy in zip(dxs, dys):
            nx, ny = dx + x, dy + y

            if can_go(nx, ny):
                push(nx, ny)
                dfs(nx, ny)

    push(start_x, start_y)
    dfs(start_x, start_y)

    # 보아하니 도착지에 visited 표시가 돼있다면 성공
    if visited[end_x][end_y]:
        return POSSIBLE
    return IMPOSSIBLE


print(solution(grid))