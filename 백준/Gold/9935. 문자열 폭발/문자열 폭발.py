s = input().strip()
bomb = input().strip()
stack = []

for char in s:
  stack.append(char)
  if len(stack) >= len(bomb):
    if ''.join(stack[-len(bomb):]) == bomb:
      for _ in range(len(bomb)):
        stack.pop()

result = ''.join(stack)
if result:
  print(result)
else:
  print("FRULA")