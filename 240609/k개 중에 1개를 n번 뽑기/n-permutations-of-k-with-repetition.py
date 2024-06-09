k, n = tuple(map(int, input().split()))

def solution(k, n):
    ans = []

    elem = []
    def choose(curr_idx):
        if curr_idx == n:
            ans.append(elem[:])
            return

        for i in range(1, k + 1):
            elem.append(i)
            choose(curr_idx + 1)
            elem.pop()

    choose(0)
    return ans

ans = solution(k, n)
for elem in ans:
    a, b = elem
    print(a, b)