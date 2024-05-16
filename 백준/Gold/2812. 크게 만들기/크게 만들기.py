N, K = map(int, input().split())
numbers = input()
stack = []

for num in numbers:
  # 스택에 있는 값이 더 작으면 삭제
  while stack and stack[-1] < num and K > 0:
    stack.pop()
    K -= 1
  stack.append(num)

if K > 0:
  print(''.join(stack[:-K])) # K가 남아있다면 더 지울 것이 남아있다는거니까 뒤에 있는걸 지운다.
else:
  print(''.join(stack))