# 15:05
n,m,c = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for i in range(n)]


def solution(m, c, grid):
    ans = -1
    n = len(grid)
    memo = [[-1] * n for i in range(n)]

    def is_possible(i,j,k,l):
        # 같은 행인데 만약 영역끼리 겹친다면
        if i == k and not (j + m <= l):
            return False
        return True
    
    arr = []
    curr_max = -1
    def choose(len_nums, nums, curr_idx):
        nonlocal curr_max

        if curr_idx == len(nums):
            # print(arr)
            if sum(arr) <= c:  # c 이하일 때만 겨루기
                # 무게 * 무게 값 구하기
                curr_val = 0
                for num in arr:
                    curr_val += (num ** 2)

                curr_max = max(curr_max, curr_val)
            return

        arr.append(nums[curr_idx])
        choose(len_nums, nums, curr_idx + 1)
        arr.pop()

        choose(len_nums, nums, curr_idx + 1)

    def get_max(x, y):
        nonlocal curr_max

        # 메모이제이션 로직 추가 1/2
        if memo[x][y] != -1:
            return memo[x][y]

        nums = grid[x][y:y + m]
        len_nums = len(nums)

        curr_max = -1
        choose(len_nums, nums, 0)
        # print(curr_max)

        # 메모이제이션 로직 추가 2/2
        memo[x][y] = curr_max
        return curr_max

    # 1. 두 도둑의 위치 완전탐색으로 지정하기
    # 2. 지정된 위치에서 m만큼의 범위 내에서 또 뽑고안뽑고 구하기(=길이무관 조합 구하기)
    # 3. 그 조합으로 가치계산 후 최대값과 겨루기
    for i in range(n):
        for j in range(n - m + 1):
            for k in range(n):
                for l in range(n - m + 1):
                    if not is_possible(i,j,k,l):
                        continue
                    # print(f'{i},{j} {k},{l}')
                    # 뽑고안뽑고 && 최대값 겨루기
                    ans = max(ans, get_max(i, j) + get_max(k, l))
    return ans


print(solution(m, c, grid))