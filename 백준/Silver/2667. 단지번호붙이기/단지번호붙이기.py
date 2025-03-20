from collections import deque
n = int(input())

# 동, 서, 남, 북
dx = [0, 0, 1, -1] #행
dy = [1, -1, 0, 0] #열
visited = [[False] * n for _ in range(n)]
answer = []

def bfs(x, y, graph):
  global answer
  q = deque()
  q.append((x, y)) 
  visited[x][y] = True
  bfs_cnt = 1

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] == 1 and not visited[nx][ny]:
          visited[nx][ny] = True # 방문 처리
          q.append((nx, ny))
          bfs_cnt += 1 # 방문했으므로 개수 증가
  
  answer.append(bfs_cnt)

graph = [list(map(int, input())) for _ in range(n)]
cnt = 0

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1 and not visited[i][j]:
      bfs(i, j, graph)
      cnt += 1

answer.sort()
print(cnt)
for i in range(len(answer)):
  print(answer[i])