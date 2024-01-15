# bfs
# 갈 수 있는 길을 queue에 넣고, 이동하면 맨 앞 값을 뺀다
# 물결모양으로 갈 수 있는 길들이 나옴 => 최소값 구하면 딘다.

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    def bfs(si, sj, ei, ej):
        # queue 초기 데이터
        v = [[0] * m for _ in range(n)]
        queue = []
        queue.append((si, sj))
        v[si][sj] = 1 # 최단 거리 계산 값 => 한 개씩 +1

        while queue:
            # 맨 앞값
            ci, cj = queue.pop(0) # 행, 열

            # 정답 처리
            if (ci, cj) == (n-1, m-1):
                return v[ci][cj]

            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = ci + di, cj + dj

                if 0<=ni<=n-1 and 0<=nj<=m-1 and maps[ni][nj] == 1 and v[ni][nj] == 0:
                    queue.append((ni, nj))                
                    v[ni][nj] = v[ci][cj] + 1
    
    ans = bfs(0, 0, n, m)
    if ans is None:
        return -1
    return ans

        