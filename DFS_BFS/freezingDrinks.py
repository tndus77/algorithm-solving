n, m = map(int, input().split()) #n은 행, m은 열
    
#2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
#dfs로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    #주어진 범위를 벗어나면 즉시 종료
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    #해당 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        #방문 처리
        graph[x][y] == 1
        #상 하 좌 우의 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False
    
#모든 노드(위치)에 따라서 음료수 채우기
count = 0 
for i in range(n):
    for j in range(m):
        #현재 위치에서 dfs 수행
        if dfs(i, j) == True: #방문 처리가 되면 True
            count += 1
            
print(count)