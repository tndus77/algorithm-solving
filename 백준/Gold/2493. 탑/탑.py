n = int(input())
lst = list(map(int, input().split()))

stack = []
result = []

for i in range(n):
  while stack:
    if stack[-1][1] > lst[i]: # 마지막 요소가 lst[i]보다 크면
      result.append(stack[-1][0] + 1)
      break
    else:
      stack.pop()
  if not stack:
    result.append(0)
  stack.append([i, lst[i]])

print(' '.join(map(str, result)))