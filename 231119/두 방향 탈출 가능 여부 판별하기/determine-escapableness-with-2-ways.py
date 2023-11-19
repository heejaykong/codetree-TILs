# 11:49
import sys
input = sys.stdin.readline
n,m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for i in range(n)]


def solution(grid):
    ans = 0
    SNAKE, NO_SNAKE = 0, 1
    n = len(grid)
    visited = [[False] * n for i in range(n)]
    sx, sy = 0, 0
    ex, ey = n-1, n-1

    def push(nx, ny):
        visited[nx][ny] = True

    def in_range(nx, ny):
        return 0 <= nx < n and 0 <= ny < m

    def can_go(nx, ny):
        if not in_range(nx, ny):
            return False
        if visited[nx][ny]:
            return False
        if grid[nx][ny] == SNAKE:
            return False
        return True

    def dfs(x, y):
        dxs, dys = [1, 0], [0, 1]
        for dx, dy in zip(dxs, dys):
            nx, ny = dx + x, dy + y
            if can_go(nx, ny):
                push(nx, ny)
                dfs(nx, ny)

    push(sx, sy)
    dfs(sx, sy)

    # dfs가 다 끝난 뒤 visited에 도착지에 도착한 이력이 있는지 확인
    POSSIBLE, IMPOSSIBLE = 1, 0
    if visited[ex][ey]:
        return POSSIBLE
    return IMPOSSIBLE


print(solution(grid))