import sys
n, k = map(int, input().split())

digit = 1
count = 9

while k > count * digit:
  if n < count:
    break
  k -= count * digit
  digit += 1
  count *= 10

start = 10 ** (digit - 1)
number = start + (k-1) // digit

if number > n:
  print(-1)
else:
  print(str(number)[(k-1) % digit])