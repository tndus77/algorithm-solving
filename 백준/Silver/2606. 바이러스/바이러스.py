computers = int(input())
node = int(input())

networks = [[] for _ in range(computers + 1)]
visited = [False] * (computers + 1)
cnt = 0

for i in range(node):
  [a, b] = list(map(int, input().split()))
  networks[a].append(b)
  networks[b].append(a)

def dfs(x):
  global cnt
  visited[x] = True

  for curr in networks[x]:
    if not visited[curr]:
      cnt += 1
      dfs(curr)

dfs(1)

print(cnt)