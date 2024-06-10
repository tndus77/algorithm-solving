from collections import deque

def solution(maps):
    # 북, 동, 남, 서
    dx = [-1, 0, 1, 0] # 행
    dy = [0, 1, 0, -1] # 열
    
    # 출발 지점 -> 레버 -> 미로빠져나가는 문
    maps = [list(map) for map in maps]
    R = len(maps)
    C = len(maps[0])
    
    def BFS(start, end):
        q = deque()
        q.append(start)
        visited = [[0] * C for _ in range(R)]
        
        while q:
            a, b = q.popleft()
            
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = visited[a][b] + 1
                    q.append((nx, ny))
        return visited[end[0]][end[1]]
            
    
    for i in range(R):
        for j in range(C):
            if maps[i][j] == 'S': start = (i, j)
            elif maps[i][j] == 'L': lever = (i, j)
            elif maps[i][j] == 'E': end = (i, j)
    dist1 = BFS(start, lever)
    dist2 = BFS(lever, end)
    return dist1 + dist2 if dist1 and dist2 else -1