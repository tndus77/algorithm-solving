import sys
board = [list(map(int, input().split())) for _ in range(19)]
# 검은색 1, 흰색 2, X 0

# 가로, 세로, 대각선
# 북, 동, 동남, 남
dx = [1, 1, 0, -1] # 행
dy = [0, 1, 1, 1] # 열
    
for i in range(19):
  for j in range(19):
    if board[i][j] != 0:
      stone = board[i][j] # 돌의 색

      for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        cnt = 1

        while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == stone:
          cnt += 1
          if cnt == 5: # 오목 됐으니 육목인지 체크하자
              # 가장 왼쪽 값 이전 값 체크
              if 0 <= i - dx[k] < 19 and 0 <= j - dy[k] < 19 and board[i-dx[k]][j-dy[k]] == stone:
                break
              # 가장 마지막 값 다음 값 체크
              if 0 <= nx + dx[k] < 19 and 0 <= ny + dy[k] < 19 and board[nx + dx[k]][ny + dy[k]] == stone:
                break
              print(stone)
              print(i+1, j+1)
              sys.exit(0)
          nx += dx[k]
          ny += dy[k]
          
print(0)