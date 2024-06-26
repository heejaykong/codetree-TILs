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











# 안녕하세요?
# 메모리 초과가 떠서 혼자 문제를 찾다 도저히 안 보여서 도움을 요청드립니다.

# 현재 칸이 바라보는 방향에 놓인 칸들을 탐색하는 과정에서 while True문을 쓰고 있기 때문에 아마 무한루프가 도는 게 아닐까 싶은데요,,,

# 암만 봐도 
# ```python
# for i in range(n):
# 	print(i)
# ```

# ```cpp
# for(int i = 0; i < n; i++)
# 	printf("%d\n", i);
# ```