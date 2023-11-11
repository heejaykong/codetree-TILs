n = int(input())
lines = [tuple(map(int, input().split())) for i in range(n)]


def solution(lines):
    n = len(lines)
    ans = -1

    def is_overlapping(arr):
        for i in range(len(arr)):
            me_x, me_y = arr[i]
            for j in range(len(arr)):
                if i == j:
                    continue
                you_x, you_y = arr[j]
                if me_x <= you_x <= me_y or me_x <= you_y <= me_y:
                    return True
        return False

    arr = []
    def choose(curr_idx):
        nonlocal ans

        if curr_idx == n:
            # 겹치는 여부 가리기
            # 안 겹치면 최대값과 겨루기
            if not is_overlapping(arr[:]):
                ans = max(ans, len(arr))
            return

        arr.append(lines[curr_idx])
        choose(curr_idx + 1)
        arr.pop()

        choose(curr_idx + 1)

    # 각 선분마다 뽑고 안뽑고를 정한 뒤(=길이무관 조합 구한 뒤)
    # 겹치는 여부 가리기
    # 안 겹치면 최대값과 겨루기
    choose(0)
    return ans


print(solution(lines))