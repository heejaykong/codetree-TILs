# O(k^n * n)
n,m,k = tuple(map(int, input().split()))
distances = list(map(int, input().split()))


def solution(destination, horse_count, distances):
    ans = 0
    arr = []
    turns_count = len(distances)


    def calc(chosen_arr):
        # print(chosen_arr, end=", ")
        nonlocal destination, horse_count

        result = 0
        scores = [0] + [1 for i in range(horse_count)]

        for turn, horse in enumerate(chosen_arr):
            # 이미 점수를 쵝득한 말이면 스루
            if scores[horse] >= destination:
                continue

            distance = distances[turn]
            scores[horse] += distance

            if scores[horse] >= destination:
                result += 1

        return result


    def choose(curr_idx):
        nonlocal horse_count, turns_count, ans

        # 2. 만들어진 순열로 점수 계산하고 max값과 겨루기
        if curr_idx == turns_count:
            ans = max(ans, calc(arr[:]))
            # print(ans)
            return

        for i in range(1, horse_count + 1):
            arr.append(i)
            choose(curr_idx + 1)
            arr.pop()


    # 1. 말들을 가지고 턴의 수만큼 중복순열 만들기
    choose(0)

    return ans


print(solution(m, k, distances))