question_k, question_n = tuple(map(int, input().split()))


def solution(k, n):
    ans = []
    arr = []

    def possible(i, curr_idx):
        if curr_idx < 2:  # 어차피 3번 셀수도 없으면 가능한 거
            return True
        if i == arr[-1] == arr[-2]:  # 3번 겹치면 안 됨
            return False
        return True


    def choose(curr_idx):
        nonlocal n

        if curr_idx == n:
            ans.append(arr[:])
            return
        
        for i in range(1, k+1):
            if not possible(i, curr_idx):
                continue

            arr.append(i)
            choose(curr_idx + 1)
            arr.pop()

    choose(0)
    return ans[:]


answer = solution(question_k, question_n)
for row in answer:
    for elem in row:
        print(elem, end=" ")
    print()