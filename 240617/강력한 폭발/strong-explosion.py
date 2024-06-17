n = int(input())
question_grid = [list(map(int, input().split())) for i in range(n)]

def solution(grid):
    BOMB, BLANK = 1, 0
    temp_grid = [[0] * len(grid) for i in range(len(grid))]
    bomb_idxs = []
    bombs_cnt = 0
    arr = []
    ans = 0


    def count_bombs(grid):
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == BOMB:
                    bomb_idxs.append((i,j))
                    cnt += 1
        return cnt


    def clear_temp_grid():
        for i in range(len(temp_grid)):
            for j in range(len(temp_grid[i])):
                temp_grid[i][j] = BLANK


    def in_range(nx, ny, leng):
        if 0 <= nx < leng and 0 <= ny < leng:
            return True
        return False


    def explode_by_type(idx, bomb_type):
        curr_x, curr_y = bomb_idxs[idx]

        if bomb_type == 1:
            dxs, dys = [0, -1, -2, 1, 2], [0, 0, 0, 0, 0]
        if bomb_type == 2:
            dxs, dys = [0, -1,  0, 1, 0], [0, 0,-1, 0, 1]
        if bomb_type == 3:
            dxs, dys = [0, -1, -1, 1, 1], [0, 1, -1, 1, -1]

        for dx, dy in zip(dxs, dys):
            nx, ny = curr_x + dx, curr_y + dy
            
            if not in_range(nx, ny, len(grid)):
                continue

            temp_grid[nx][ny] = BOMB
            


    def simulate_explosion():
        nonlocal bombs_cnt

        clear_temp_grid()
    
        for i, bomb_type in enumerate(arr):
            explode_by_type(i, bomb_type)
        
        return count_bombs(temp_grid)


    def choose(curr_idx):
        nonlocal bombs_cnt, ans

        if curr_idx == bombs_cnt:
            # 2. 폭발 시뮬레이션 돌려서 터지는 영역 개수 세기
            destroyed_size = simulate_explosion()

            # 3. 터지는 영역 개수 겨루기
            ans = max(ans, destroyed_size)
            return

        for i in range(1, 3 + 1):
            arr.append(i)
            choose(curr_idx + 1)
            arr.pop()


    # 1-1. 폭탄 위치 개수 세기
    bombs_cnt = count_bombs(grid)

    # 1-2. 폭탄 위치 개수만큼의 길의를 지닌, 1~3(폭발유형)으로 이뤄진 중복순열
    choose(0)

    return ans


print(solution(question_grid))