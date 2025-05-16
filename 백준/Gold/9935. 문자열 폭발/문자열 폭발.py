import sys
input = sys.stdin.readline

s = input().strip()
bomb = input().strip()
stack = []

for char in s:
  stack.append(char)
  if char == bomb[-1] and len(stack) >= len(bomb):
    if ''.join(stack[-len(bomb):]) == bomb:
      for _ in range(len(bomb)):
        stack.pop()

result = ''.join(stack)
print(result if result else 'FRULA')