n = int(input())
array = list(map(int, input().split()))

#가장 큰수를 고르고 
#한칸 띄어진 값 중 가장 큰 값 고르기
d = [0] * 103

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(array[i-1], array[i-2] + array[i])
    
print(d[n-1])