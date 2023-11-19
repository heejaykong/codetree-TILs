# 12:20
import sys
from collections import deque
input = sys.stdin.readline
n, k = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for i in range(n)]
starts = [tuple(map(int, input().split())) for i in range(k)]

def solution(grid, starts):
    ans = 0
    BLANK, WALL = 0, 1
    n = len(grid)
    k = len(starts)
    visited = [[False] * n for i in range(n)]
    q = deque()

    def push(x, y):
        nonlocal ans
        visited[x][y] = True
        q.append((x, y))
        ans += 1
    
    def in_range(nx, ny):
        return 0 <= nx < n and 0 <= ny < n
    
    def can_go(nx, ny):
        if not in_range(nx, ny):
            return False
        if visited[nx][ny]:
            return False
        if grid[nx][ny] == WALL:
            return False
        return True

    def bfs():
        dxs, dys = [0,1,0,-1], [1,0,-1,0]
        while q:
            x, y = q.popleft()

            for dx, dy in zip(dxs, dys):
                nx, ny = dx + x, dy + y

                if can_go(nx, ny):
                    push(nx, ny)

    for r, c in starts:
        push(r-1, c-1)
    bfs()

    return ans


print(solution(grid, starts))