# 나무의 수, 상근이가 가져가려는 나무 길이
N, M = map(int, input().split())
lst = list(map(int, input().split()))
start, end = 0, max(lst)

while start <= end:
  mid = (start + end) // 2 # 상한가
  sum = 0 # 상근이가 가져갈 수 있는 나무 길이
  for num in lst:
    if num >= mid:
      sum += num - mid # 상근이가 가져갈 수 있는 나무 길이
    else:
      sum += 0 # 상한가보다 낮으면 상관없음
  
  if M > sum:
    # 상근이가 나무를 더 많이 가져갈 수 있도록 상한가를 짧게
    # 끝값 감소
    end = mid - 1
  else:
    # 상근이가 나무를 못가져가도록 상한가를 올려야한다.
    start = mid + 1

print(end)
