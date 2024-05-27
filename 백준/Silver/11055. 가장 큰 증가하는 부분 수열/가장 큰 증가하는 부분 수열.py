n = int(input())
lst = list(map(int, input().split()))
dp = [1 for _ in range(n)]
dp[0] = lst[0]

for i in range(1, n):
  for j in range(i):
    if lst[i] > lst[j]:
      dp[i] = max(dp[i], dp[j] + lst[i])
    else:
      dp[i] = max(dp[i], lst[i])

print(max(dp))