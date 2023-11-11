n,m = tuple(map(int, input().split()))
infos = [tuple(map(int, input().split())) for i in range(m)]


def solution(n, infos):
    MAX = 15 + 1
    ans = MAX
    # 사다리타기 알고리즘을 위해 선분정보 가공하고 정렬하기
    lines = []
    for a, b in infos:
        lines.append((b, a-1))
    lines.sort()

    def is_same(res1, res2):
        for i in range(len(res1)):
            original = res1[i]
            selected = res2[i]
            if not original == selected:
                return False
        return True

    def simulate(arr):
        nonlocal n
        res = [ppl for ppl in range(1, n + 1)]
        for _, idx in arr:
            res[idx], res[idx + 1] = res[idx + 1], res[idx]
        return res[:]

    len_lines = len(lines)
    arr = []
    def choose(curr_idx):
        nonlocal ans

        if curr_idx == len_lines:
            # 초기 결과랑 같은지 확인
            if is_same(simulate(lines), simulate(arr[:])):
                ans = min(ans, len(arr))
            return

        arr.append(lines[curr_idx])
        choose(curr_idx + 1)
        arr.pop()

        choose(curr_idx + 1)

    # 선분들 중 뽑고 안뽑고(=길이 무관 조합) 구한 뒤
    # 초기 결과랑 같은지 확인
    # 초기 결과랑 같다면 최소값과 겨루기
    choose(0)
    return ans

print(solution(n, infos))