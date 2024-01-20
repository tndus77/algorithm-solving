n = int(input())
cnt = 0

def solution(input):
  global cnt
  if input < 100:
    return input
  
  cnt = 99
  for i in range(100, n+1):
    a = i // 100
    b = (i // 10) % 10
    c = i % 10
    if b - a == c - b:
      cnt += 1
  return cnt
    
print(solution(n))