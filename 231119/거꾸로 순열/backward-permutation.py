n = int(input())


def solution(n):
    ans = []
    nums = [i for i in range(n, 0, -1)]
    visited = [False] * (n + 1)

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

    # 중복순열(for문이용) 로직 그대로 사용하되
    # visited를 활용하면 중복없는 순열을 만들 수 있다
    # 순서를 거꾸로 출력하기 위해 nums를 거꾸로 정렬하면 될듯
    choose(0)

    return ans


ans = solution(n)
for row in ans:
    for el in row:
        print(el, end=" ")
    print()