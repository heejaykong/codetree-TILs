# 00:47
n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]


def solution(grid):
    n = len(grid)
    visited_cols = [False] * n
    ans = -1
    curr_sum = 0

    arr = []
    def choose(curr_leng):
        nonlocal ans, curr_sum
 
        if curr_leng == n:
            ans = max(ans, curr_sum)
            return
 
        for i in range(n):
            if visited_cols[i]:
                continue

            curr_sum += grid[curr_leng][i]
            visited_cols[i] = True

            choose(curr_leng + 1)

            curr_sum -= grid[curr_leng][i]
            visited_cols[i] = False

    # 행은 고려 안하고 열만 고려해도 충분한 문제였음,,,
    # 중복없는 순열을 만들려면,
    # 중복순열 로직(for문사용)에 visited만 얹어주면 된다
    # 만약 append하려는 대상이 이미 visited된 열이라면 스루해야 함
    # 다 만들어진 순열의 합을 구해 최대값과 겨루기
    choose(0)
    return ans


print(solution(grid))