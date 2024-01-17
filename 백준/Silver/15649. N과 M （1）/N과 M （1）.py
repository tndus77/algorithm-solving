n, m = map(int, input().split())
s = []

def dfs():
  #리스트에 들어간 수열들이 m개가 되면 나온다.
  if len(s) == m:
    print(' '.join(map(str, s)))
  else:
    for i in range(1, n+1):
      if i not in s:
        s.append(i)
        dfs() #m개의 수열이 완성 되었는지 검열하기 위해서
        s.pop()

dfs()