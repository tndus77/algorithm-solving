# 2+1 세일
# 가장 싼 것을 무료로 지불
# 비싼건 비싼거끼리 살때 가장 최소 금액이다. 왜냐면 가장 싼게 비싼 가격이니까

N = int(input())
dairys = [int(input()) for _ in range(N)]
dairys = sorted(dairys, reverse=True)

ans = 0

for i in range(0, len(dairys), 3):
  if i+2 < len(dairys):
    # 이미 dairys[i+1]가 가장 최솟값
    ans += dairys[i] + dairys[i+1]
  else: # 3개 안삼
    ans += sum(dairys[i:])

print(ans)