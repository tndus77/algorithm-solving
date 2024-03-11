import sys
import heapq
input = sys.stdin.readline

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
time.sort()

Q = []
heapq.heappush(Q, time[0][1]) # 현재 강의의 끝나는 시간

for i in range(1, n):
  if time[i][0] < Q[0]: # 다음 강의의 시작 시간이 현재 끝나는 시간보다 작으면
    heapq.heappush(Q, time[i][1]) # 강의실 하나 추가
  else:
    heapq.heappop(Q) # 현재 들어있는 종료 시간 꺼내기
    heapq.heappush(Q, time[i][1]) # 다시 새로운 종료 시간으로 갱신

print(len(Q))
