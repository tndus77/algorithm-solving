
def solution(n, computers):
    answer = 0
    
    visited = [0] * n
    
    def dfs(N):
        visited[N] = 1
        
        for i in range(n):
            if N == i:
                continue
            if computers[N][i] == 1 and not visited[i]:
                dfs(i)
        
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1

    return answer