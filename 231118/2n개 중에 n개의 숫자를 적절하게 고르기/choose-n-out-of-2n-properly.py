# 18:19
n = int(input())
nums = list(map(int, input().split()))


def solution(nums):
    n = len(nums) // 2
    len_nums = len(nums)
    total_sum = sum(nums)
    MAX = total_sum + 1
    ans = MAX

    def calc_diff(group):
        sum1 = sum(group)
        sum2 = total_sum - sum(group)
        return abs(sum1 - sum2)

    arr = []
    def choose(num_idx, curr_leng):
        nonlocal ans

        if curr_leng == n:
            ans = min(ans, calc_diff(arr[:]))
            return
        if num_idx == len_nums:
            return
        
        arr.append(nums[num_idx])
        choose(num_idx + 1, curr_leng + 1)
        arr.pop()

        choose(num_idx + 1, curr_leng)

    # nums중 n 길이만큼의 뽑고안뽑고(조합)을 구한 뒤,
    # 현조합 원소들, 그 외 원소들의 합의 차를 구하고
    # 최소값과 겨루기
    choose(0, 0)

    return ans


print(solution(nums))