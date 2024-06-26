n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
directions = [list(map(int, input().split())) for i in range(n)]
r, c = tuple(map(int, input().split()))


def solution(grid, directions, r, c):
    ans = 0
    n = len(grid)
    dxs = [0,-1,-1, 0, 1, 1, 1, 0,-1]
    dys = [0, 0, 1, 1, 1, 0,-1,-1,-1]


    def in_range(nx, ny):
        nonlocal n
        if 0 <= nx < n and 0 <= ny < n:
            return True
        return False


    def get_bigger_cells(r, c):
        d = directions[r][c]
        cells = []
        me = grid[r][c]

        while True:
            nx = r + dxs[d]
            ny = c + dys[d]
            # print(d, nx, ny)

            if not in_range(nx, ny):
                break
            
            # 다음 칸이 나보다 크면 갈 수 있음
            if grid[nx][ny] > me:
                cells.append((nx, ny))
            
            r, c = nx, ny

        return cells[:]


    def choose(r, c, curr_count):
        nonlocal ans

        # 매번 갱신(끝이 명확한 문제가 아니므로)
        ans = max(ans, curr_count)

        # 바라보는 방향에 지금보다 큰 숫자를 지닌 칸들을 구한다
        cells = get_bigger_cells(r,c)
        # print(cells)

        if len(cells) == 0:  # 더 이상 갈 곳이 없을 때
            return

        for next_r, next_c in cells:
            choose(next_r, next_c, curr_count + 1)


    choose(r-1, c-1, 0)
    return ans


print(solution(grid, directions, r, c))