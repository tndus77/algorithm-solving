from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    def dfs(idx):
        visited[idx] = True
        
        for i in range(n):
            if not visited[i] and computers[idx][i]: # 방문 X & 연결되어있어
                dfs(i)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1 # dfs 끝나면 answer + 1
    return answer

