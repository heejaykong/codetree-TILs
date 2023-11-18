n,m = tuple(map(int, input().split()))


def solution(n,m):
    nums = [i for i in range(1, n + 1)]
    ans = []

    arr = []
    def choose(num_idx, curr_leng):
        if curr_leng == m:
            ans.append(arr[:])
            return
        if num_idx == n:
            return
        
        arr.append(nums[num_idx])
        choose(num_idx + 1, curr_leng + 1)
        arr.pop()

        choose(num_idx + 1, curr_leng)

    choose(0, 0)
    return ans

ans = solution(n,m)
for row in ans:
    for el in row:
        print(el, end=' ')
    print()