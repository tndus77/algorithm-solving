R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0] # 행
dy = [0, 1, 0, -1] # 열

max_len = 0

def dfs(x, y, visited, count):
  global max_len
  
  max_len = max(max_len, count)

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    # 다른 알파벳이고, 방문을 안했다면
    if 0 <= nx < R and 0 <= ny < C:
      char = board[nx][ny]
      idx = ord(char) - ord('A')

      if not (visited & (1 << idx)):
        dfs(nx, ny, visited | (1 << idx), count + 1)

start_char = board[0][0]
start_bit = 1 << (ord(start_char) - ord('A'))
dfs(0, 0, start_bit, 1)
print(max_len)