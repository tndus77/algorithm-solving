import sys

def bfs(si, sj, ei, ej):
    v = [[0] * m for _ in range(n)]
    q = []

    q.append((si, sj)) # 초깃값 세팅
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0) # pop한 현재값

        # 종료 조건
        if (ci, cj) == (ei, ej):
            return v[ei][ej]

        for di, dj in (-1, 0), (1, 0), (0, -1), (0, 1):
            ni = ci + di
            nj = cj + dj

            if 0<=ni<=n-1 and 0<=nj<=m-1 and arr[ni][nj] == 1 and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
ans = bfs(0, 0, n - 1, m - 1)
print(ans)
