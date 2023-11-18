# 00:47
n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]


def solution(grid):
    n = len(grid)
    visited_rows = [False] * n
    visited_cols = [False] * n  # (그냥 2차원으로 visited 만들수도 있겠지만 나중에 행이랑 열 계산하는게 귀찮아서 걍 행용 열용 따로 만듦) 
    ans = -1

    # 순열로 만들 대상 초기화
    pos = []
    for i in range(n):
        for j in range(n):
            pos.append((i, j))
    len_pos = len(pos)

    def calc(arr):
        total = 0
        for x, y in arr:
            total += grid[x][y]
        return total

    arr = []
    def choose(curr_leng):
        nonlocal ans
 
        if curr_leng == n:
            ans = max(ans, calc(arr[:]))
            return
 
        for i in range(len_pos):
            row, col = pos[i]

            if visited_rows[row] or visited_cols[col]:
                continue

            arr.append(pos[i])
            visited_rows[row] = True
            visited_cols[col] = True

            choose(curr_leng + 1)

            arr.pop()
            visited_rows[row] = False
            visited_cols[col] = False

    # 각 i,j 칸 단위로 중복이 없는 순열을 만든다
    # 중복없는 순열을 만들려면,
    # 중복순열 로직(for문사용)에 visited만 얹어주면 된다
    # 만약 append하려는 대상이 이미 visited된 행이나 열이라면 스루해야 함
    # 다 만들어진 순열의 합을 구해 최대값과 겨루기
    choose(0)
    return ans


print(solution(grid))