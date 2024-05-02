import sys

N = int(input())
words = [list(input().split()) for _ in range(N)]
dict = dict()

for word in words:
  arr = str(word)[2:-2].split('.')
  if dict.get(arr[1]): # 값이 있으면
    dict[arr[1]] = dict.get(arr[1]) + 1
  else:
    dict[arr[1]] = 1

for key, value in sorted(dict.items()):
  print(key, value)