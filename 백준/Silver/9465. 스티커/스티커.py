import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  m = int(input())
  sticker = [list(map(int, input().split())) for _ in range(2)]
  dp = [[0] * m for _ in range(2)]

  # 스티커 길이가 1인 경우
  dp[0][0] = sticker[0][0]
  dp[1][0] = sticker[1][0]
  if m == 1:
    print(max(dp[0][0], dp[1][0]))
    continue

  # 스티커 길이가 2인 경우
  dp[0][1] = dp[1][0] + sticker[0][1]
  dp[1][1] = dp[0][0] + sticker[1][1]
  if m == 2:
    print(max(dp[0][1], dp[1][1]))
    continue

  # 3 이상인 경우
  for i in range(2, m):
    dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + sticker[0][i]
    dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + sticker[1][i]

  print(max(dp[0][-1], dp[1][-1]))