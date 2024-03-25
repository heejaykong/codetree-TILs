k, n = 2, 3
ans = []

def choose(leng):
    global k, n, ans

    if leng == n:
        print(ans)
        return
    
    for i in range(1, k + 1):

        if leng > 1 and i == ans[leng-1] and ans[leng-1] == ans[leng-2] and ans[leng-2] == i:
            return
        ans.append(i)
        choose(leng + 1)
        ans.pop()

choose(0)