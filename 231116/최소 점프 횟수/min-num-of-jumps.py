# 21:48
n = int(input())
nums = list(map(int, input().split()))


def solution(nums):
    MAX = 10 * 4 + 1
    ans = MAX
    count = 0

    len_nums = len(nums)
    def choose(curr_idx, jump_length):
        nonlocal ans, count
        # print(f'me: {curr_idx},{jump_length}')

        if curr_idx == len_nums - 1:
            ans = min(ans, count)
            return
        
        for i in range(1, jump_length + 1):
            if (curr_idx + i) >= len_nums:  # 범위 벗어나면 스루
                continue
            count += 1
            choose(curr_idx + i, nums[curr_idx + i])
            count -= 1


    # 현재 인덱스 기준 최대점프범위 이내만큼
    # 뽑고안뽑고 수행
    # 끝에 도달하면, 최소값 겨루기
    choose(0, nums[0])

    if ans == MAX:
        return -1
    return ans


print(solution(nums))