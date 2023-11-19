# 13:23
import sys
input = sys.stdin.readline
n = int(input())


def solution(n):
    MAX = 1000
    MOD = 10007
    dp = [-1] * (MAX + 1)

    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    for i in range(4, n + 1):
        dp[i] = dp[i-2] + dp[i-3]

    if dp[n] == -1:
        return 0
    return dp[n] % MOD


print(solution(n))