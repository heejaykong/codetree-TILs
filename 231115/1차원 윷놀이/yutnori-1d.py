n,m,k = tuple(map(int, input().split()))
turns = list(map(int, input().split()))


def solution(m, k, turns):
    ans = -1
    n = len(turns)
    horses = [1 for _ in range(k)]

    def calc(horses):
        count = 0
        for horse in horses:
            if horse >= m:
                count += 1
        return count

    def choose(curr_idx):
        nonlocal ans

        # 유의: 아래 for문 속 if문 때문에
        # 얘는 매 재귀마다 최대값과 겨뤄줘야 함
        ans = max(ans, calc(horses[:]))

        if curr_idx == n:
            return
        for i in range(k):
            # 이미 점수를 딴 말이면 스루
            if horses[i] >= m:
                continue

            dist = turns[i]
            horses[i] += dist
            choose(curr_idx + 1)
            horses[i] -= dist

    # 1. n길이의, 1~k를 원소로 지닌 중복순열 만들기
    # 2. 그 순열 원소가 곧 말이 되어... 점수 계산하기
    # 3. 점수로 최대값 겨루기
    choose(0)

    return ans


print(solution(m, k, turns))