# 16:04
import sys
n = int(input())
grid = [list(input()) for i in range(n)]

def solution(grid):
    nums = [i for i in range(1, 9+1)]
    n = len(grid)
    MAX = sys.maxsize
    ans = MAX

    # 시작점, 끝점, 동전위치매퍼 초기화
    start_x, start_y = 0, 0
    end_x, end_y = 0, 0
    mapper = {}
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'S':
                start_x, start_y = i, j
                continue
            if grid[i][j] == 'E':
                end_x, end_y = i, j
                continue
            if grid[i][j] != '.':
                coin = int(grid[i][j])
                mapper[coin] = (i, j)
    # print(mapper)

    def find_path(coins):
        # print(coins)
        before_x, before_y = start_x, start_y
        dist = 0

        for coin in coins:  # 3개 동전 찾아가유...
            # 유의: 주어진 조합의 원소 중 현재 매퍼에 없는지 먼저 확인해야 함
            if coin not in mapper:
                return MAX

            after_x, after_y = mapper[coin]
            curr_dist = abs(after_x - before_x) + abs(after_y - before_y)
            dist += curr_dist
            before_x, before_y = after_x, after_y

        # 마지막 동전에서 끝점 찾아가유...
        after_x, after_y = end_x, end_y
        curr_dist = abs(after_x - before_x) + abs(after_y - before_y)
        dist += curr_dist
        return dist

    len_nums = len(nums)
    arr = []
    def choose(num_idx, curr_leng):
        nonlocal ans

        if curr_leng == 3:
            # 실제 그래프에서 길을 찾아본 뒤,
            # 가능하다면 최소값과 겨루기
            ans = min(ans, find_path(arr[:]))
            return
        if num_idx == len_nums:
            return

        arr.append(nums[num_idx])
        choose(num_idx + 1, curr_leng + 1)
        arr.pop()

        choose(num_idx + 1, curr_leng)

    # 서로 다른 동전 3개 챙겨야 하니까 조합으로 해야 함
    # 오름차순 조합을 구한 뒤,
    # 실제 그래프에서도 그렇게 찾아갈 수 있는지 탐색하기
    # 가능하면 최소값과 겨루기
    choose(0, 0)

    if ans == MAX:
        return -1
    return ans

print(solution(grid))