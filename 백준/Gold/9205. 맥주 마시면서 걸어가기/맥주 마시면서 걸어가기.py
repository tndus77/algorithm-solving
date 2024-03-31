import sys
from collections import deque

def bfs(sx, sy, rx, ry):
  q = deque()
  v = [0] * n

  q.append((sx, sy))

  while q:
    x, y = q.popleft()

    if abs(x - rx) + abs(y - ry) <= 1000: # 락 페스티벌에 도착 가능한 상태
      return 'happy'

    for i in range(n): # 편의점 이동
      if v[i] == 0:
        ni, nj = conv_st[i]

      if abs(x - ni) + abs(y - nj) <= 1000:
        q.append((ni, nj))
        v[i] = 1

  return 'sad'

t = int(input())
for _ in range(t):
  n = int(input()) # 편의점 갯수

  sx, sy = map(int, input().split()) # 상근이네 집
  conv_st = [list(map(int, input().split())) for _ in range(n)] # 편의점
  rx, ry = map(int, input().split()) # 페스티벌

  ans = bfs(sx, sy, rx, ry)
  print(ans)