# 오랜만에 하느라 코테 다 까먹어서 해설보고 함

MAX = 100 * 100
ans = MAX

n = int(input())
HALF = n // 2
grid = [list(map(int, input().split())) for i in range(n)]
evening = [False for i in range(n)]

def calc():
    morning_sum = 0
    evening_sum = 0

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            if not evening[i] and not evening[j]:
                morning_sum += grid[i][j]

            if evening[i] and evening[j]:
                evening_sum += grid[i][j]

    return abs(morning_sum - evening_sum)

def choose(curr_idx, leng):
    global ans

    # 1. 전체 일 중 HALF개만큼 조합 만들기
    if leng == HALF:
        # 2. 그 조합으로 업무강도 계산하고 최솟값과 겨루기
        ans = min(ans, calc())
        return
    if curr_idx == n:
        return
    
    choose(curr_idx + 1, leng)

    evening[curr_idx] = True
    choose(curr_idx + 1, leng + 1)
    evening[curr_idx] = False

    return ans


print(choose(0, 0))