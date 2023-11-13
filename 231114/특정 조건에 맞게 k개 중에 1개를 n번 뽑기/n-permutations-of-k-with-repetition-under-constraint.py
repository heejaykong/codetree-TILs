k,n = tuple(map(int, input().split()))


def solution(k,n):
    ans = []

    arr = []
    nums = [i for i in range(1, k + 1)]
    def choose(curr_idx):
        if curr_idx == n:
            ans.append(arr[:])
            return
        for num in nums:
            # 그런데 이제 append시 조건을 곁들인
            # 현재 적어도 2번째 인덱스를 고르고 있으며,
            # 전 원소와 전전 원소가 지금 뽑으려는 숫자와 하필 같다면, 스루
            if curr_idx >= 2 and (num == arr[-1] and arr[-1] == arr[-2]):
                continue
            arr.append(num)
            choose(curr_idx + 1)
            arr.pop()

    choose(0)
    return ans


ans = solution(k,n)
for row in ans:
    for cell in row:
        print(cell, end=' ')
    print()