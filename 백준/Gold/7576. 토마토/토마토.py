from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

count = 0
q = deque([])

for i in range(m):
  for j in range(n):
    if graph[i][j] == 1:
      q.append([i, j])

# 북, 동, 남, 서
dx = [-1, 0, 1, 0] #행
dy = [0, 1, 0, -1] #열
def bfs():
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y] + 1
        q.append([nx, ny])

bfs()
ans = 0
for line in graph:
  for tomato in line:
    if tomato == 0: # 익지 못했으므로
      print(-1)
      exit(0)
  ans = max(ans, max(line))

print(ans-1) # 처음 익은 토마토가 1로 시작하기 때문에