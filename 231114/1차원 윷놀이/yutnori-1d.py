n,m,k = tuple(map(int, input().split()))
turns = list(map(int, input().split()))


def solution(m, k, turns):
    ans = -1
    n = len(turns)
    horses = [i for i in range(1, k + 1)]

    def calc(arr):
        next_horses = {}
        count = 0
        for i, dist in enumerate(turns):
            me = arr[i]

            # 만약 첨 움직이는 말이면 처음값 집어넣기
            if me not in next_horses:
                next_horses[me] = 1 + dist
            # 만약 아는 말인데 이미 점수를 땄던 말이면 스루
            elif next_horses[me] >= m:
                continue
            # 그 외엔 걍 평범하게 옮겨주기
            else:
                next_horses[me] += dist

            # 그러고보니 이놈이 점수를 땄다면 카운트 증가
            if next_horses[me] >= m:
                count += 1

        return count

    arr = []
    def choose(curr_idx):
        nonlocal ans

        if curr_idx == n:
            ans = max(ans, calc(arr[:]))
            return
        for horse in horses:
            arr.append(horse)
            choose(curr_idx + 1)
            arr.pop()

    # 1. n길이의, 1~k를 원소로 지닌 중복순열 만들기
    # 2. 그 순열 원소가 곧 말이 되어... 점수 계산하기
    # 3. 점수로 최대값 겨루기
    choose(0)

    return ans


print(solution(m, k, turns))