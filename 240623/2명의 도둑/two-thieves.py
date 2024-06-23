# 복잡도는 O(n**(2*2) * 2**m)
question_n, question_m, question_c = map(int, input().split())
question_grid = [list(map(int, input().split())) for i in range(question_n)]

def solution(m, c, grid):
    ans = 0
    max_sum = 0
    n = len(grid)


    def choose(curr_idx, curr_value, curr_sum, bag):
        nonlocal m, c, max_sum

        if curr_idx == m:
            if curr_sum <= c:
                # print(curr_value)
                max_sum = max(max_sum, curr_value)
            return

        elem = bag[curr_idx]

        curr_sum += elem
        curr_value += (elem * elem)
        choose(curr_idx + 1, curr_value, curr_sum, bag)
        curr_sum -= elem
        curr_value -= (elem * elem)

        choose(curr_idx + 1, curr_value, curr_sum, bag)


    # 1. 2중포문 두 번 돌면서 격자 내 안겹치는 m길이 짝 구하기
    for i in range(n):
        for j in range(n):

            if not (j + m <= n):  # m길이 잴 때 격자 벗어나면 안 됨
                continue

            for k in range(n):
                for l in range(n):

                    if not (l + m <= n):
                        continue

                    # 짝끼리 겹치면 안 됨
                    if i == k:
                        if (j <= l < j + m) or (l <= j < l + m):
                            continue
                    
                    bag1 = grid[i][j:j+m]
                    bag2 = grid[k][l:l+m]

                    # 2. 그 짝으로, 각각 조합 구하기
                    # (조합 원소합이 C 이하여야 함)
                    max_sum = 0
                    choose(0, 0, 0, bag1)
                    value1 = max_sum
                    # print("bag1", bag1, value1)
                    
                    max_sum = 0
                    choose(0, 0, 0, bag2)
                    value2 = max_sum
                    # print("bag2", bag2, value2)

                    # 3. 매 조합이 뱉는 총 가치로 max값 겨루기
                    ans = max(ans, value1 + value2)
                    # print(ans)
                    # print()
    return ans


print(solution(question_m, question_c, question_grid))