k,n = tuple(map(int, input().split()))

def solution(k,n):
    nums = [i for i in range(1, k + 1)]
    len_nums = len(nums)
    ans = []

    arr = []
    def choose(leng):
        if leng == n:
            ans.append(arr[:])
            return
        
        for num in nums:
            arr.append(num)
            choose(leng + 1)
            arr.pop()

    choose(0)

    return ans


ans = solution(k,n)
for row in ans:
    for cell in row:
        print(cell, end=" ")
    print()