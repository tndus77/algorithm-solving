N, K = map(int, input().split())

arr = [[0] * N for _ in range(N+1)]

for i in range(N+1):
  for j in range(N):
    if j == 0 or j == N-1:
      arr[i][j] = 1
    else:
      arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
print(arr[N-1][K-1])