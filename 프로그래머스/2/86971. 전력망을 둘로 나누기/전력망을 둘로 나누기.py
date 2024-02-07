from collections import deque

def solution(n, wires):
    node = [[] for _ in range(n+1)]
    res = 0
    
    for i in range(n-1):
        [start, end] = wires[i]
        node[start].append(end)
        node[end].append(start)
    
    def bfs(start):
        visited = [0] * (n+1)
        q = deque([start])
        visited[start] = 1
        cnt = 1
        
        while q:
            s = q.popleft()
            for i in node[s]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = 1
                    cnt += 1
        return cnt 
    
    res = n # 선을 제거하기 전에 연결된 노드의 개수의 차이가 최대가 될 수 있도록 보장
    for a,b in wires:
        node[a].remove(b)
        node[b].remove(a)
        
        res = min(abs(bfs(a)-bfs(b)), res)
        
        node[a].append(b)
        node[b].append(a)
    return res