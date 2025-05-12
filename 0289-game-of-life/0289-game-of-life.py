import copy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # 8번, 왼쪽부터 시계방향
        dx = [0, -1, -1, -1, 0, 1, 1, 1] # 행
        dy = [-1, -1, 0, 1, 1, 1, 0, -1] # 열

        # 행, 열
        n, m = len(board), len(board[0])
        final_board = copy.deepcopy(board)

        for x in range(n):
            for y in range(m):
                # 1 주변에 2개 or 3개면 1로 유지
                # 1 주변에 1이 3개 초과 시 0으로
                # 0 주변에 1이 3개 있으면 1로
                live_cnt = 0
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < n and 0 <= ny < m:
                        if board[nx][ny] == 1:
                            live_cnt += 1
                if board[x][y] == 1:
                    if live_cnt < 2 or live_cnt > 3:
                        final_board[x][y] = 0
                else:
                    if live_cnt == 3:
                        final_board[x][y] = 1
        
        for i in range(n):
            for j in range(m):
                board[i][j] = final_board[i][j]