# 20:48
n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]


def solution(grid):
    NO_BOMB, BOMB = 0, 1
    n = len(grid)
    destroy = [[NO_BOMB] * n for i in range(n)]
    ans = -1

    # 폭탄이 놓여야만 하는 곳들을 찾아 배열에 저장
    bombs = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == BOMB:
                bombs.append((i,j))

    def log(target):
        for i in range(n):
            for j in range(n):
                print(target[i][j], end=' ')
            print()

    def in_range(x, y):
        return 0 <= x < n and 0 <= y < n
    
    def drop_bomb(spot, bomb_type):
        # 타입에 따라 다르게 그려주기
        x, y = spot
        destroy[x][y] = BOMB
        if bomb_type == 1:  # 세로 일직선 두칸씩만
            dxs, dys = [1,-1,2,-2], [0,0,0,0]
            for dx, dy in zip(dxs, dys):
                nx, ny = dx + x, dy + y
                if not in_range(nx, ny):
                    continue
                destroy[nx][ny] = BOMB
        elif bomb_type == 2:  # 십자가 한칸씩만
            dxs, dys = [0,1,0,-1], [1,0,-1,0]
            for dx, dy in zip(dxs, dys):
                nx, ny = dx + x, dy + y
                if not in_range(nx, ny):
                    continue
                destroy[nx][ny] = BOMB
        elif bomb_type == 3:  # 꼭지점 한칸씩만
            dxs, dys = [1,-1,1,-1], [1,1,-1,-1]
            for dx, dy in zip(dxs, dys):
                nx, ny = dx + x, dy + y
                if not in_range(nx, ny):
                    continue
                destroy[nx][ny] = BOMB

    def simulate(types):
        # 일단 연습장 초기화
        for i in range(n):
            for j in range(n):
                destroy[i][j] = NO_BOMB
        # 실제로 터뜨리기
        for i in range(len(bombs)):
            curr_spot = bombs[i]
            curr_type = types[i]
            # print(f'from{curr_spot} with {curr_type}')
            drop_bomb(curr_spot, curr_type)
            # log(destroy)
        # 얼마나 초토화시켰는지 개수 세기
        count = 0
        for i in range(n):
            for j in range(n):
                if destroy[i][j] == BOMB:
                    count += 1
        
        return count

    arr = []
    len_bombs = len(bombs)
    def choose(curr_idx):
        nonlocal ans

        if curr_idx == len_bombs:
            # 해당 순열에 맞춰 폭탄 터뜨려보기(초기화한 destroy에 기록)
            # 그리고 최대값과 겨루기
            ans = max(ans, simulate(arr[:]))
            return
        for bomb_type in [1, 2, 3]:
            arr.append(bomb_type)
            choose(curr_idx + 1)
            arr.pop()
    
    # len(bombs) 길이의 중복순열 만들기
    choose(0)

    return ans

print(solution(grid))