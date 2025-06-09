from collections import deque

def bfs(n, k):
    max_limit = 100001
    q = deque([n])
    visited = [0] * max_limit
    
    while q:
        current = q.popleft()

        if current == k:
            # 이동 횟수
            return visited[current]
        
        for next_pos in (current-1, current+1, 2*current):
            if 0 <= next_pos < max_limit and visited[next_pos] == 0:
                visited[next_pos] = visited[current] + 1
                q.append(next_pos)

# n -> k
n, k = map(int, input().split())
print(bfs(n, k))