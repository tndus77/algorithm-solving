import sys

# 이미 가지고 있는 랜선의 개수, 필요한 랜선의 개수
K, N = map(int, input().split())
lst = [int(input()) for _ in range(K)]
start, end = 0, max(lst)

while start <= end:
  mid = (start + end) // 2
  sum = 0

  for num in lst:
    if mid == 0:
      sum += num
    else:
      sum += num // mid # 현재 길이에서 얻을 수 있는 랜선 총 갯수
  
  if N > sum:
    # 랜선을 더 가져야해!
    # 상한가를 낮춘다.
    end = mid - 1
  else:
    # 랜선 너무 많이 가졌어
    # 상한가를 더 높게 가진다.
    start = mid + 1
  
print(end)