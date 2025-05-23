T = int(input())

dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

def loop(n):
  if dp[n] != 0:
    return dp[n]
  return loop(n-1) + loop(n-2) + loop(n-3)

for _ in range(T):
  n = int(input())

  print(loop(n))