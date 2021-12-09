from collections import deque

n, m = map(int, input().split()) #n은 행, m은 열

#2차원 리스트의 맵 정보 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
#이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#bfs 소스코드 구현
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue: #queue가 빌때까지
        x, y = queue.popleft()
        #방문 처리 되지 않은 것 넣기
            #방향 처리 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #미로를 벗어났을 떄 
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            #벽인 경우 제외 
            if graph[nx][ny] == 0:
                continue
            
            #해당 노드를 처음 방문하는 경우에만 최단 거리 이용
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

        #가장 오른쪽 아래의 최단 거리 반환
    return graph[n-1][m-1]
    
print(bfs(0, 0))
            
        
        
