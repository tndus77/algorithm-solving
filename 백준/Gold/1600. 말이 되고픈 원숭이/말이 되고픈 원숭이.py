import sys
from collections import deque

input = sys.stdin.readline
# 원숭이는 K번만 말처럼 움직일 수 있고, 그 외에는 인접한 칸으로만
K = int(input())
M, N = map(int, input().split()) # 열, 행
arr = [list(map(int, input().split())) for _ in range(N)]

# 0은 평지, 1은 장애물
# 장애물이 있는 곳으로는 이동할 수 없다.
# 도착점에 갈 수 없는 경우엔 -1

# 특정한 이동 방식에 횟수가 정해져있을 때, 3차원 배열을 이용한다.
# 즉, 방문 처리 배열을 3차원 배열
# visited[열][행][이동수]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0] # 행
dy = [0, 1, 0, -1] # 열
horse_dx = [-2, -1, 1, 2, 2, 1, -1, -2]
horse_dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(n):
  q = deque()
  q.append((0, 0, n))
  visited = [[[0] * (n+1) for _ in range(M)] for _ in range(N)]
  
  while q:
    x, y, cnt = q.popleft()

    if x == N-1 and y == M-1: # 도달하면
      return visited[x][y][cnt]

    if cnt > 0: # 말처럼 이동 가능
      for i in range(8):
        nx = x + horse_dx[i]
        ny = y + horse_dy[i]

        if 0 <= nx < N and 0 <= ny < M:
          if arr[nx][ny] != 1 and visited[nx][ny][cnt-1] == 0: # 다음 값이 0일 때 = 방문 안했을 때
            visited[nx][ny][cnt-1] = visited[x][y][cnt] + 1
            q.append((nx, ny, cnt-1))

    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]

      if 0 <= nx < N and 0 <= ny < M:
        if arr[nx][ny] != 1 and visited[nx][ny][cnt] == 0:
          visited[nx][ny][cnt] = visited[x][y][cnt] + 1
          q.append((nx, ny, cnt))
  return -1

result = bfs(K)
print(result)