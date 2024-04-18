import sys
input = sys.stdin.readline
from collections import deque

# 수빈이, 동생
N, K = map(int, input().split())
limit = 100001
visited = [False] * limit
cnt = [0] * limit

# 수빈 => 걷거나 순간이동 가능
# 1초 후 X-1 or X+1, 순간이동 0초 후에 2*X

def bfs(x, end):
  q = deque()
  q.append(x)

  while q:
    x = q.popleft()

    if x == end:
      return cnt[x]
    
    if -1 < 2*x < limit and visited[2*x] == False:
      q.append(2*x)
      cnt[2*x] = cnt[x]
      visited[2*x] = True
    if -1 < x-1 < limit and visited[x-1] == False:
      q.append(x-1)
      cnt[x-1] = cnt[x] + 1
      visited[x-1] = True
    if -1 < x+1 < limit and visited[x+1] == False:
      q.append(x+1)
      cnt[x+1] = cnt[x] + 1
      visited[x+1] = True

print(bfs(N, K))