question_n = int(input())
question_lines = [tuple(map(int, input().split())) for i in range(question_n)]


def solution(lines):
    n = len(lines)
    arr = []
    ans = 0

    def is_overlapping(leng):
        for i in range(leng):
            my_x, my_y = arr[i]

            for j in range(leng):
                if i >= j:
                    continue

                other_x, other_y = arr[j]

                if my_x <= other_x <= my_y or my_x <= other_y <= my_y or \
                    other_x <= my_x <= other_y or other_x <= my_y <= other_y:
                    return True

        return False
    
    # 1. 길이가 n이하인 모든 조합 만들기
    def choose(lines_idx, leng):
        nonlocal n, ans

        if lines_idx == n:
            # 2. 겹치는지 확인
            if not is_overlapping(leng):
                # 3. 안 겹치면 max값과 겨루기
                ans = max(ans, leng)
            return
        
        arr.append(lines[lines_idx])
        choose(lines_idx + 1, leng + 1)
        arr.pop()

        choose(lines_idx + 1, leng)
    
    choose(0, 0)
    return ans


print(solution(question_lines))