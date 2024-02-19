import sys
sys.stdin = open("/Users/sooyeon/AlgorithmSolving/Python/input.txt", "r")
input = sys.stdin.readline

r, c = map(int, input().split())

lst = [list(map(str, input())) for _ in range(r)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0] # 행
dy = [0, 1, 0, -1] # 열

arr = []
ans = 0

def dfs(x, y, count):
  global ans

  ans = max(count, ans)
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < r and 0 <= ny < c and lst[nx][ny] not in arr:
      # 가자!
      arr.append(lst[nx][ny])
      dfs(nx, ny, count + 1)
      arr.remove(lst[nx][ny])

arr.append(lst[0][0])
dfs(0, 0, 1)

print(ans)

# 배열은 시간초과, set()은 가능? 