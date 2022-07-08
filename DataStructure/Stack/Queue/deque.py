import sys
from collections import deque

n = int(input())
queue = deque()

def empty():
    if len(queue) == 0:
        return 1
    else:
        return 0
    
def size():
    return len(queue)

for i in range(n):
    command = list(input().split())
    
    if command[0] == "push_back":
        queue.append(command[1])
    elif command[0] == "push_front":
        queue.appendleft(command[1])
    elif command[0] == "pop_front":
        if empty() == 1:
            print("-1")
        else:
            print(queue.popleft())
    elif command[0] == "pop_back":
        if empty() == 1:
            print("-1")
        else:
            print(queue.pop())
    elif command[0] == "size":
        print(size())
    elif command[0] == "empty":
        if empty() == 1:
            print("1")
        else:
            print("0")
    elif command[0] == "front":
        if empty() == 1:
            print("-1")
        else:
            print(queue[0])
    elif command[0] == "back":
        if empty() == 1:
            print("-1")
        else:
            print(queue[-1])