from collections import deque

n = int(input())
lst = deque([i+1 for i in range(n)])

while lst:
  if len(lst) == 1:
    break
  first_pop = lst.popleft()
  second_pop = lst.popleft()
  lst.append(second_pop)

print(''.join(map(str, list(lst))))