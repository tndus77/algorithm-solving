def cal(a, b, op):
  if op == '+':
    return a + b
  if op == '*':
    return a * b
  if op == '-':
    return a - b

def dfs(idx, current):
  global max_val
  
  # 종료 조건
  if idx >= len(exp):
    max_val = max(max_val, current)
    return
  
  # 괄호 추가 X
  dfs(idx+2, cal(current, int(exp[idx]), exp[idx-1]))

  # 괄호 추가 O
  if idx + 2 < len(exp):
    # 뒤에 값 계산
    temp = cal(int(exp[idx]), int(exp[idx+2]), exp[idx+1])
    dfs(idx+4, cal(current, temp, exp[idx-1]))

n = int(input())

exp = list(input())
max_val = -float('inf')

dfs(2, int(exp[0]))
print(max_val)