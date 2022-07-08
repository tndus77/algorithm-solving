##각 행마다 가장 작은 수를 찾은 뒤 그 수 중 가장 큰 수를 찾으면 된다
#min함수 사용

n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    #현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    #비교 
    result = max(result, min_value)
    
print(result)