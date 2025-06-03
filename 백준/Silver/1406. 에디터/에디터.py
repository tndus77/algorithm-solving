import sys
from collections import deque

input = sys.stdin.readline

left_stack = deque(list(input().strip()))
M = int(input())

right_stack = deque()

for _ in range(M):
    command = list(input().split())
    
    if command[0] == 'P':
        left_stack.append(command[1])
    elif command[0] == 'L' and left_stack:
            right_stack.appendleft(left_stack.pop())
    elif command[0] == 'B' and left_stack:
            left_stack.pop()
    elif command[0] == 'D' and right_stack:
            left_stack.append(right_stack.popleft())

print(''.join(left_stack) + ''.join(right_stack))