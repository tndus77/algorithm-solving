import sys
sys.stdin = open("/Users/sooyeon/AlgorithmSolving/Python/input.txt", "r")
n = int(input())

total = 0

while True:
  if n % 5 == 0:
    total += n // 5
    break
  else:
    n -= 2
    total += 1

  if n < 0:
    break

if n < 0:
  print(-1)
else:
  print(total)