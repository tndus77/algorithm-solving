def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(x):
        visited[x] = True
        
        if x == n:
            return
        
        for i in range(n):
            if not visited[i] and computers[x][i] == 1:
                dfs(i)
        
    for i in range(len(computers)):
        if not visited[i] and computers[i][i] == 1:
            dfs(i)
            answer += 1
            
    return answer