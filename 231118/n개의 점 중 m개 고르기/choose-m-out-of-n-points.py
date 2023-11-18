# 18:44
n,m = tuple(map(int, input().split()))
dots = [tuple(map(int, input().split())) for i in range(n)]


def solution(dots, m):
    len_dots = len(dots)
    MAX = 100 * 2 + 100 * 2  # 절대 안될 값으로 대강 산정한 것임
    ans = MAX

    arr = []
    def choose(dot_idx, curr_leng):
        if curr_leng == m:
            print(arr)
            return
        if dot_idx == len_dots:
            return

        arr.append(dots[dot_idx])
        choose(dot_idx + 1, curr_leng + 1)
        arr.pop()

        choose(dot_idx + 1, curr_leng)

    # 주어진 점들 중 m개의 뽑고안뽑고(조합)을 구한 뒤,
    # 그 조합 중 최대 거리값을 구하고,
    # 최소값과 겨루기
    choose(0, 0)

    return ans


print(solution(dots, m))