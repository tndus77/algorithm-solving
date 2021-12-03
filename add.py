#가장 큰 수와 두 번째로 큰 수 저장
#공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

#n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))
first = data[n-1] #가장 큰 수
second = data[n-2] #두 번째로 큰 수 

result = 0

while True:
    for i in range(k): #가장 큰 수를 k번 더하기
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second #두 번째로 큰 수를 한 번 더하기 
    m -= 1
    
print(result)

#####
##더 효율적인 코드로 짜보자
#반복되는 수열에 대해서 파악해야한다.
#int(m/(k+1))*k 앞에는 수열이 반복되는 횟수, k를 곱해주면 가장 큰 수가 등장하는 횟수
# +(m%(k+1)) m이 나누어떨어지지 않는 경우 고려

##int(m/(k+1)*k)+(m%(k+1))
n, m, k = map(int, input().split)
data = list(map(int, input().split))

data.sort() #데이터 정렬
first = data[n-1]
second = data[n-2]

#가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1))*k
count += m%(k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)

##파이썬에서는 A를 B로 나눈 몫을 구하기 위해 int(A/B) or A//B 라고 작성한다.