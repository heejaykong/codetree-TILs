# 20:08
n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
directions = [list(map(int, input().split())) for i in range(n)]
r, c = tuple(map(int, input().split()))


def solution(grid, directions, r, c):
    ans = -1
    n = len(grid)
    dxs = [0,  -1,-1,0,1,1,1,0,-1]
    dys = [0,  0,1,1,1,0,-1,-1,-1]

    def in_range(nx, ny):
        return 0 <= nx < n and 0 <= ny < n

    def can_go(nx, ny, me):
        if not in_range(nx, ny):
            return False
        if grid[nx][ny] <= me:
            return False
        return True
    
    count = 0
    def choose(x, y):
        nonlocal count, ans

        ans = max(ans, count)  # 매 재귀때마다 갱신해야 하므로 아묻따 최대값 겨루기

        dirr = directions[x][y]
        # print(f'me: {grid[x][y]}')
        
        for i in range(1, n):
            nx, ny = (dxs[dirr] * i) + x, (dys[dirr] * i) + y

            if can_go(nx, ny, grid[x][y]):
                # print(grid[nx][ny])
                count += 1
                choose(nx, ny)
                count -= 1
        

    # 현재 바라보는 방향으로,
    # 조건만 만족한다면,
    # 뽑고안뽑고 수행하기
    # 뽑을때마다 카운트값 증가시키고 최대값과 겨루기
    choose(r-1, c-1)

    return ans


print(solution(grid, directions, r, c))