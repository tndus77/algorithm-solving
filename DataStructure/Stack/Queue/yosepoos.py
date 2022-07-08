from collections import deque

n, k = map(int, input().split())
q = deque(x for x in range(1, n+1))

print('<', end='')
for i in range(n):
    q.rotate(1-k)
    
    if i != n-1: #끝에 도달하지 않으면
         print(q.popleft(), end= ', ')
    else:
        print(q.popleft(), end = '')
print('>')