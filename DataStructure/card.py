#1부터 입력받은 자연수만큼 들어있는 큐 배열을 만든다.
#큐 길이가 1이 될때까지 반복
    #맨 앞에 원소를 제거
    #맨 앞에 원소를 맨 뒤로 보낸다
import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque(i for i in range(1, n+1))

while len(queue) > 1:
    #가장 맨 앞에 있는 것을 빼고 
    queue.popleft() 
    #가장 맨 앞에 있는 카드를 맨 뒤로 옮긴다
    queue.append(queue.popleft())
    
print(queue.pop())