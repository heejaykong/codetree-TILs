n,m = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

def solution(m, nums):
    n = len(nums)
    ans = -1

    def calc(arr):
        if m == 1:
            return arr[0]
        val = arr[0]
        for el in arr[1:]:
            val ^= el
        return val

    arr = []
    def choose(num_idx, curr_leng):
        nonlocal ans
        if curr_leng == m:
            ans = max(ans, calc(arr[:]))
            return
        if num_idx == n:
            return
        
        arr.append(nums[num_idx])
        choose(num_idx + 1, curr_leng + 1)
        arr.pop()

        choose(num_idx + 1, curr_leng)

    # xor연산은 순서에 영향을 받지 않으므로
    # 길이가 정해진 뽑고안뽑고(조합)를 만들어 계산해
    # 최대값과 겨루면 됨
    choose(0, 0)

    return ans


print(solution(m, nums))