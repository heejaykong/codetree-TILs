question_input = int(input())

def solution(n):
    arr = []
    ans = 0

    def is_beautiful(arr):
        curr_num = arr[0]
        curr_count = 1

        for i, num in enumerate(arr[1:]):
            if curr_num != num:
                # 만약 조건(해당 숫자만큼 연달아 같은 숫자가 나오기)을 위반하면 더 이상 볼 것도 없음
                if curr_count % curr_num != 0:
                    return False
                # 초기화
                curr_num = num
                curr_count = 1
                continue

            curr_count += 1

        if curr_count % curr_num == 0:
            # print(arr)
            return True

        return False


    def choose(curr_idx):
        nonlocal ans
        if curr_idx == n:
            if is_beautiful(arr):
                ans += 1
            return
        
        for i in range(1, 4+1):
            arr.append(i)
            choose(curr_idx + 1)
            arr.pop()

    choose(0)

    return ans


print(solution(question_input))