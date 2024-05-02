import sys
input = sys.stdin.readline

ducklist = list(input().strip())
ans = 0

if ducklist[0] != 'q' or ducklist[-1] != 'k' or len(ducklist) % 5:
  print(-1)
  exit()

def quack(start):
  global ans
  duck = 'quack'
  j = 0
  flag = True # 새로운 오리로 생성해라

  for i in range(start, len(ducklist)):
    if ducklist[i] == duck[j]:
      if ducklist[i] == 'k': # 끝에 도달했으면
        if flag:
          ans += 1
          flag = False # k로 끝났으니 새로운 오리로 생성할 필요 X
        j = 0
        ducklist[i] = 0
        continue
      j+= 1
      ducklist[i] = 0

for i in range(len(ducklist) - 4):
  if ducklist[i] == 'q':
    quack(i)

if any(ducklist) or ans == 0:
  print(-1)
else:
  print(ans)