MAX = 1000000000
MIN = -1000000000
ans_max = MIN
ans_min = MAX

n = int(input())
nums = list(map(int, input().split()))
counts = list(map(int, input().split()))
ops = ['+', '-', '*']
ans = nums[0]


def calc(op, num):
    global ans
    if op == '+':
        ans += num
    if op == '-':
        ans -= num
    if op == '*':
        ans *= num
    return ans


def calc_backwards(op, num):
    global ans
    if op == '+':
        ans -= num
    if op == '-':
        ans += num
    if op == '*':
        ans //= num
    return ans


def choose(idx, leng):
    global ans, ans_min, ans_max

    if leng == n-1:
        ans_min = min(ans, ans_min)
        ans_max = max(ans, ans_max)
        return
    if idx == n-1:
        return
    
    for i in range(len(ops)):
        if counts[i]:

            ans = calc(ops[i], nums[idx+1])  # ans.append(ops[i])
            counts[i] -= 1

            choose(idx + 1, leng + 1)
            
            ans = calc_backwards(ops[i], nums[idx+1])  # ans.pop()
            counts[i] += 1
        
        else:
            choose(idx + 1, leng)


choose(0,0)
print(ans_min, ans_max)