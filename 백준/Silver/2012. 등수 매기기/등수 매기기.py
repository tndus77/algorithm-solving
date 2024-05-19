import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()

result = 0
for i in range(1, n+1):
  result += abs(i - lst[i-1])

print(result)