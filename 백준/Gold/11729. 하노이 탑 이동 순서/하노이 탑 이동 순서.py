N = int(input())
move = []

def hanoi_tower(n, _from, to, other):
  if n == 0:
    return
  # 1단계: 1 -> 2, n-1 모두
  hanoi_tower(n-1, _from, other, to)
  # 2단계: 1 -> 3 
  move.append([_from, to])
  # 3단계: 2 -> 3
  hanoi_tower(n-1, other, to, _from)


hanoi_tower(N, 1, 3, 2)
print(len(move))

for i in range(len(move)):
  print(move[i][0], move[i][1])