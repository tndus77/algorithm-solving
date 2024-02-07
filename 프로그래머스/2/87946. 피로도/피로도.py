answer = 0

def dfs(k, cnt, dungeons, visited):
    global answer
    if cnt > answer:
        answer = cnt

    # 최소 피로도, 소모 피로도
    for i in range(len(dungeons)):
        [minimum, consume] = dungeons[i]
        if not visited[i] and k >= minimum:
            visited[i] = True
            dfs(k-consume, cnt+1, dungeons, visited) 
            visited[i] = False
                
def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    
    dfs(k, 0, dungeons, visited)
    
    return answer