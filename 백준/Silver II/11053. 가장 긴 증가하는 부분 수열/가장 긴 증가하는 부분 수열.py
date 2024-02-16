n = int(input())
lst = list(map(int, input().split()))

# dp 배열 초기화
dp = [1] * len(lst)

# 각 위치에서의 가장 긴 증가하는 부분 수열 길이 계산
for i in range(n):
  for j in range(i):
    if lst[i] > lst[j]:
      dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))