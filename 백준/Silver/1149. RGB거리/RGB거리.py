n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]

# dp[i][0] = i번까지 집을 빨강으로 칠할 때 최소 비용
# dp[i][1] = i번까지 집을 초록으로 칠할 때 최소 비용
# dp[i][2] = i번까지 집을 파랑으로 칠할 때 최소 비용
dp[0] = lst[0]

for i in range(1, n):
  dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + lst[i][0]
  dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + lst[i][1]
  dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + lst[i][2]

print(min(dp[n-1]))