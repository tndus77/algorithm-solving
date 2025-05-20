n = int(input())
dp = [0 for _ in range(n+1)]
T = []
P = []

for i in range(n):
  day, cost = map(int, input().split())
  T.append(day)
  P.append(cost)
  
for i in range(n-1, -1, -1):
  # 오늘 시작되는 상담을 했을 때 끝나지 않은 경우 - 참여 x
  if i+T[i] > n : # 상담에 필요한 일수가 퇴사일을 넘어가면
    dp[i] = dp[i+1] # 다음날 값 그대로 가져옴
  else:
    dp[i] = max(dp[i+1], dp[i+T[i]]+P[i]) #오늘 상담을 안할 경우와 상담을 할 경우 중 max 값

print(dp[0])