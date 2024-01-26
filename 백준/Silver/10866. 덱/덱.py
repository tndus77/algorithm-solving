import sys
from collections import deque

n = int(input())
queue = deque()

for i in range(n):
  arr = sys.stdin.readline().split()

  if arr[0] == 'push_front':
    queue.appendleft(arr[1])
  elif arr[0] == 'push_back':
    queue.append(arr[1])
  elif arr[0] == 'pop_front':
    if queue:
      print(queue[0])
      queue.popleft()
    else:
      print(-1)
  elif arr[0] == 'pop_back':
    if queue:
      print(queue[-1])
      queue.pop()
    else:
      print(-1)
  elif arr[0] == 'size':
    print(len(queue))
  elif arr[0] == 'empty':
    if queue:
      print(0)
    else:
      print(1)
  elif arr[0] == 'front':
    if queue:
      print(queue[0])
    else:
      print(-1)
  elif arr[0] == 'back':
    if queue:
      print(queue[-1])
    else:
      print(-1)

  