import sys

input = sys.stdin.readline

def dfs(node, parent):
    global is_tree
    visited[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, node)
        # 방문 처리가 되어있는데 부모가 아니다?
        elif neighbor != parent:
            is_tree = False

case_num = 1
while True:
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break
    
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    cnt = 0
    is_tree = True

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1, N+1):
        if not visited[i]:
            is_tree = True
            dfs(i, -1)
            if is_tree:
                cnt += 1
    
    if is_tree:
        if cnt == 1:
            print(f'Case {case_num}: There is one tree.')
        else:
            print(f'Case {case_num}: A forest of {cnt} trees.')
    else:
        print(f'Case {case_num}: No trees.')

    case_num += 1