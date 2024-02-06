from collections import deque

# 숫자가 클수록 중요도가 높은 것
n = int(input())

for i in range(n):
  N, M = map(int, input().split()) #N은 갯수, M은 궁금한 문서
  queue = deque(map(int, input().split()))
  queue = deque([(idx, i) for idx, i in enumerate(queue)])
  count = 0

  while True:
    if queue[0][1] == max(queue, key=lambda x:x[1])[1]:
      # 어차피 나올 것이니까 count 시작!
      count += 1
  
      if queue[0][0] == M: # 궁금한 문서의 인덱스와 같은지
        print(count)
        break
      else:
        queue.popleft()
    else:
      queue.append(queue.popleft())