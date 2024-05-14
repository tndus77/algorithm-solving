import sys

T = int(input())

for t in range(T):
  N = int(input())
  num = list(map(int, input()))
  lst = list(input())
  ans = 0

  for i in range(len(lst)):
    if lst[i] == '*':
      ans += 1
    else: # #일 경우
      if i == 0:
        if num[i] != 0 and num[i+1] != 0:
          num[i] -= 1
          num[i+1] -= 1
          ans += 1
      elif i == N - 1:
        if num[i] != 0 and num[i-1] != 0:
          num[i] -= 1
          num[i-1] -= 1
          ans += 1
      else: # 중간
        if num[i-1] != 0 and num[i] != 0 and num[i+1] != 0:
          num[i-1] -= 1
          num[i] -= 1
          num[i+1] -= 1
          ans += 1
  print(ans)
