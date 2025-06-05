import sys
import heapq

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
dp = [[[float('inf')] * 3 for _ in range(M)] for _ in range(N)]

# 첫 행에서 각 위치에 도달하는 경우
for j in range(M):
    for d in range(3):
        dp[0][j][d] = lst[0][j]

for i in range(1, N):
    for j in range(M):
        for d in range(3):
            nj = j + (d-1)

            if 0 <= nj < M:
                for pd in range(3):
                    if d != pd:
                        dp[i][j][d] = min(dp[i][j][d], dp[i-1][nj][pd] + lst[i][j])
print(min(dp[N-1][j][d] for j in range(M) for d in range(3)))