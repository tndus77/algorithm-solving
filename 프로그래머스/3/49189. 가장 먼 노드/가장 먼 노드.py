from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    distance = [-1] * (n+1)
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(graph):
        q = deque()
        q.append(1) # 현재 노드, 이동한 거리
        distance[1] = 0 # 출발 노드의 최단 거리를 0으로
        
        while q:
            cur = q.popleft()
            
            for node in graph[cur]:
                if distance[node] == -1:
                    distance[node] = distance[cur] + 1
                    q.append(node)
    bfs(graph)
    
    for d in distance:
        if d == max(distance):
            answer += 1
    return answer