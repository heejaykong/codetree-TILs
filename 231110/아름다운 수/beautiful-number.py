n = int(input())


def solution(n):
    nums = [i for i in range(1, 4+1)]
    ans = 0

    def is_beautiful(arr):
        # 1333221 -> O
        # 111 -> O
        # 212 -> X
        # 222 -> X
        is_wrong = False
        i = 0
        while i < len(arr):
            if is_wrong:
                break

            num = arr[i]
            count = num
            
            for j in range(count):
                if i + j >= len(arr):
                    is_wrong = True
                    break
                curr_num = arr[i + j]
                if curr_num != num:
                    is_wrong  = True
                    break
            i += count

        if not is_wrong:
            return True
        return False

    arr = []
    def choose(curr_idx):
        nonlocal ans

        if curr_idx == n:
            # 아름다운 수가 맞다면 정답++
            if is_beautiful(arr[:]):
                ans += 1
            return
        
        for num in nums:
            arr.append(num)
            choose(curr_idx + 1)
            arr.pop()

    # n자리 중복 순열 만들기
    choose(0)

    return ans


print(solution(n))