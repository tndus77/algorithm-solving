import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)

# 재귀 - Top-down 방식
def rec(n):
    if dp[n] != 0:
        return dp[n]
    if n == 1:
        return 0

    if n % 3 == 0 and n % 2 == 0:
        dp[n] = min(rec(n//3) + 1, rec(n//2) + 1)
    elif n % 3 == 0:
        dp[n] = min(rec(n-1)+1, rec(n//3)+1)
    elif n % 2 == 0:
        dp[n] = min(rec(n-1)+1, rec(n//2)+1)
    else:
        dp[n] = rec(n-1) + 1
    return dp[n]

print(rec(N))