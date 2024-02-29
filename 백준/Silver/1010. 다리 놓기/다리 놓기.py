import math

n = int(input())

for _ in range(n):
  n, m = map(int, input().split())

  print(math.comb(m, n))