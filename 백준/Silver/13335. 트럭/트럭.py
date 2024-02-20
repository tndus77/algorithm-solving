from collections import deque

# 트럭 갯수, 다리 길이, 다리 최대하중
n, w, l = map(int, input().split())
trucks = deque(list(map(int, input().split())))

bridge = deque([0] * w)
time = 0

while bridge:
  time += 1
  bridge.popleft()
  
  if trucks:
    if sum(bridge) + trucks[0] <= l:
      bridge.append(trucks.popleft())
    else:
      bridge.append(0)

print(time)