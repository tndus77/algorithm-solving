T = int(input())

for i in range(1, T+1):
  n = int(input())
  # 시작 값 선언
  cnt_0 = [1, 0]
  cnt_1 = [0, 1]

  for i in range(2, n+1):
    cnt_0.append(cnt_0[i-1] + cnt_0[i-2])
    cnt_1.append(cnt_1[i-1] + cnt_1[i-2])
  print(cnt_0[n], cnt_1[n])
