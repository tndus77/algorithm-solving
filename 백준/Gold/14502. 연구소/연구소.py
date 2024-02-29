from collections import deque
import copy

# 세로, 가로
n, m = map(int, input().split())
virus = [list(map(int, input().split())) for _ in range(n)]

# 벽을 3개 다 세우면, 바이러스 분출

# 북, 동, 남, 서
dx = [-1, 0, 1, 0] #행
dy = [0, 1, 0, -1] #열

def bfs():
  global ans
  # 칠해버리기
  q = deque()
  tmp = copy.deepcopy(virus)

  for i in range(n):
    for j in range(m):
      if tmp[i][j] == 2:
        q.append((i, j)) # 바이러스
  
  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

      if tmp[nx][ny] == 0:
        tmp[nx][ny] = 2
        q.append((nx, ny))

  cnt = 0
  for item in tmp:
    cnt += item.count(0)
  ans = max(ans, cnt)

def make_wall(cnt):
  if cnt == 3:
    bfs()
    return
  
  for i in range(n):
    for j in range(m):
      if virus[i][j] == 0: # 빈공간이라면 벽 세우기 가능
        virus[i][j] = 1
        make_wall(cnt+1)
        virus[i][j] = 0 # 벽 해제

ans = 0
make_wall(0)
print(ans)