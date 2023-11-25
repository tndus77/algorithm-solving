def solution(n, computers):
    answer = 0
    m = len(computers[0])
    v = [False for _ in range(n)]
    
    def DFS(x):
        v[x] = True
        
        for j in range(m):
            if computers[x][j] == 1 and v[j] == False:
                DFS(j)
    
    
    for i in range(n):
        if v[i] == False:
            DFS(i)
            answer += 1
    return answer

