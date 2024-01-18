n = int(input())
arr = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())
maximum = -1e9
minimum = 1e9

def dfs(idx, sum, plus, minus, multiply, divide):
  global maximum, minimum
  if idx == n:
    maximum = max(sum, maximum)
    minimum = min(sum, minimum)
    return
  
  if plus:
    dfs(idx+1, sum + arr[idx], plus - 1, minus, multiply, divide)
  if minus:
    dfs(idx+1, sum - arr[idx], plus, minus-1, multiply, divide)
  if multiply:
    dfs(idx+1, sum * arr[idx], plus, minus, multiply-1, divide)
  if divide:
    dfs(idx+1, int(sum / arr[idx]), plus, minus, multiply, divide-1)

dfs(1, arr[0], plus, minus, multiply, divide)
print(maximum)
print(minimum)