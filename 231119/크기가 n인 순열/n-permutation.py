n = int(input())


def solution(n):
    nums = [i for i in range(1, n + 1)]
    visited = [False] * (n + 1)
    ans = []

    arr = []
    def choose(curr_leng):
        if curr_leng == n:
            ans.append(arr[:])
            return
        for i in range(n):
            if visited[nums[i]]:
                continue
            arr.append(nums[i])
            visited[nums[i]] = True
            choose(curr_leng + 1)
            arr.pop()
            visited[nums[i]] = False

    # 중복순열 로직에서, visited를 추가한 로직이면
    # 중복이 없는 순열을 만들 수 있음
    choose(0)

    return ans


ans = solution(n)
for row in ans:
    for el in row:
        print(el, end=" ")
    print()