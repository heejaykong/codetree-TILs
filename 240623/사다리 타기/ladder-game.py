question_n, question_m = map(int, input().split())
question_lines = [tuple(map(int, input().split())) for i in range(question_m)]

def solution(n, given_lines):
    MAX = 16; ans = MAX
    m = len(given_lines)
    arr = []

    def play_game(n, lines):
        sorted_lines = sorted(lines, key=lambda x: (x[1], x[0]))
        result = [i for i in range(n + 1)]

        for nth, _ in sorted_lines:
            result[nth], result[nth + 1] = result[nth + 1], result[nth]

        return result


    def choose(lines_idx, leng):
        nonlocal m, ans

        if lines_idx == m:
            # 2. 사다리 태워보고 원래 결과와 동일한지 확인
            # 3. 동일하면 min값 겨루기
            made_result = play_game(n, arr)
            if given_result == made_result:
                ans = min(leng, ans)
            return
        
        arr.append(given_lines[lines_idx])
        choose(lines_idx + 1, leng + 1)
        arr.pop()

        choose(lines_idx + 1, leng)


    given_result = play_game(n, given_lines)
    # 1. 길이가 m 이하인 조합 만들기
    choose(0, 0)

    return ans


print(solution(question_n, question_lines))