k, n = tuple(map(int, input().split()))

def solution(k, n):
    ans = []

    arr = []
    def choose(curr_idx):
        if curr_idx == n:
            ans.append(arr[:])
            return

        for i in range(1, k + 1):
            arr.append(i)
            choose(curr_idx + 1)
            arr.pop()

    choose(0)
    return ans

ans = solution(k, n)
for arr in ans:
    for elem in arr:
        print(elem, end=" ")
    print()