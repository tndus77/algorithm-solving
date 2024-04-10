import sys
input = sys.stdin.readline
from collections import deque

# 이동 가능 => .
# 이동 불가 => #
# 열쇠 => 소문자, 문 => 대문자
# 민식이 => 0, 출구 => 1

# 북, 동, 남, 서
dx = [-1, 0, 1, 0] # 행
dy = [0, 1, 0, -1] # 열

N, M = map(int, input().split())
arr = [list(map(str, input().rstrip())) for _ in range(N)]
visited = [[[0] * 64 for _ in range(M)] for _ in range(N)]
q = deque()

for i in range(N):
  for j in range(M):
    if arr[i][j] == "0":
      arr[i][j] = '.'
      q.append((i, j, 0))
      break

while q:
  a, b, key = q.popleft()

  for i in range(4):
    nx = a + dx[i]
    ny = b + dy[i]
    nkey = key

    if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != '#' and visited[nx][ny][key] == 0:
      # 문인 경우
      # and 연산
      # key가 없는 경우 버린다.
      if arr[nx][ny].isupper():
        if not (key & 1 << (ord(arr[nx][ny]) - ord('A'))):
          continue
      # 열쇠인 경우
      # or 연산
      # key 교체
      elif arr[nx][ny].islower():
        nkey |= 1 << ord(arr[nx][ny]) - ord('a')
      elif arr[nx][ny] == "1":
        print(visited[a][b][key] + 1)
        exit()
      q.append((nx, ny, nkey))
      visited[nx][ny][nkey] = visited[a][b][key] + 1

print(-1)