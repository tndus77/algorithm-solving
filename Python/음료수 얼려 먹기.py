import sys
sys.stdin = open("/Users/sooyeon/AlgorithmSolving/Python/input.txt", "r")

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
count = 0

# 북, 동, 남, 서
dx = [-1, 0, 1, 0] #행
dy = [0, 1, 0, -1] #열

def dfs(x, y):
  graph[x][y] = 1

  # stack 사용
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx > -1 and ny > -1 and nx < n and ny < m:
      # 인접 노드에 음료 채울 수 있는지 확인
      if graph[nx][ny] == 0:
        # 인접 노드 이동
        dfs(nx, ny)

for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      dfs(i, j)
      count += 1
print(count)