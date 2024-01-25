n = int(input())
aArr = list(map(int, input().split()))
m = int(input())
bArr = list(map(int, input().split()))

aArr.sort() # 탐색하려는 배열이 무조건 정렬되어있어야 한다!

for i in bArr:
  find = False

  start, end = 0, n - 1
  while start <= end:
    mid = (start + end) // 2

    if aArr[mid] == i:
      find = True
      break
    elif aArr[mid] < i:
      start = mid + 1
    else:
      end = mid - 1

  if find:
    print(1)
  else:
    print(0)