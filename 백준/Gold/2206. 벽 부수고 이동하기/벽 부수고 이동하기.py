import sys
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
#0은 이동 가능, 1은 벽

# 북, 동, 남, 서
dx = [-1, 0, 1, 0] # 행
dy = [0, 1, 0, -1] # 열
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

def bfs(xi, yi, count):
  q = deque()
  q.append((xi, yi, count))

  while q:
    x, y, K = q.popleft()

    # 끝 점에 도달하면
    if x == N - 1 and y == M - 1:
      return visited[x][y][K]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      # 다음 이동할 곳이 벽이고 count가 남아있으면 부수기 가능
      if arr[nx][ny] == 1 and K == 0:
        visited[nx][ny][1] = visited[x][y][0] + 1
        q.append((nx, ny, 1))
      # 다음 이동할 곳이 이동 가능하고, 아직 한 번도 방문하지 않은 곳이라면
      if arr[nx][ny] == 0 and visited[nx][ny][K] == 0:
        visited[nx][ny][K] = visited[x][y][K] + 1
        q.append((nx, ny, K))

  return -1

print(bfs(0, 0, 0))