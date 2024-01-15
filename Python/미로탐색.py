import sys
sys.stdin = open("/Users/sooyeon/AlgorithmSolving/Python/input.txt", "r")

from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0] #행
dy = [0, 1, 0, -1] #열

#최소의 칸 수 구하는 프로그램
def bfs(start_x, start_y):
  queue = deque()
  queue.append((start_x, start_y))

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 벗어날 경우
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      
      # 벽일 경우
      if graph[nx][ny] == 0:
        continue
      
      # 벽이 아닐 경우
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  return graph[n-1][m-1]
print(bfs(0, 0))