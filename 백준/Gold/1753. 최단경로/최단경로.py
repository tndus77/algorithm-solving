import sys
import heapq
input = sys.stdin.readline

# 정점의 개수, 간선의 개수
n, e = map(int, input().split())
m = int(input())
graph = [[] * (n+1) for _ in range(n+1)]
heap = []
INF = int(1e9)
distance = [INF] * (n+1)

for _ in range(e):
  u, v, w = map(int, input().split())

  graph[u].append((w, v))

def dijkstra(start):
   # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
   distance[start] = 0
   heapq.heappush(heap, (0, start))

   while heap:
      # 가장 최단 경로인 노드에 대한 정보 꺼내기
      dist, now = heapq.heappop(heap)

      # 현재 노드가 처리 됐다면 skip
      if distance[now] < dist:
         continue
      
      for wei, i in graph[now]:
         cost = dist + wei

         if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(heap, (cost, i))
      
       
dijkstra(m)

for i in range(1, n+1):
  if distance[i] == INF:
     print('INF')
  else:
     print(distance[i])
