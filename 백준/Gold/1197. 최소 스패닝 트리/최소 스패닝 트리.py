import sys
import heapq

input = sys.stdin.readline
V, E = map(int, input().split())

graph = [[] for _ in range((V+1))]
visited = [False] * (V+1)
result = 0

for _ in range(E):
    a, b, w = map(int,input().split())
    graph[a].append([w, b])
    graph[b].append([w, a])

heap = [[0, 1]]
while heap:
    w, curr_node = heapq.heappop(heap)

    if not visited[curr_node]:
        visited[curr_node] = True
        result += w

        for next_node in graph[curr_node]:
            if not visited[next_node[1]]:
                heapq.heappush(heap, next_node)

print(result)