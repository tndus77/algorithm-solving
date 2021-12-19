n, k = map(int, input().split())

arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

arrayA.sort()
arrayB.sort(reverse=True)

#첫번째 인덱스부터 확인하며, 두 배열의 원소를 최대 k번 비교
for i in range(k):
    if arrayA[i] < arrayB[i]:
        arrayA[i], arrayB[i] = arrayB[i], arrayA[i]
    else: #배열 a의 원소 값이 b보다 더 크거나 같을 때, 반복문 탈출
        break
    
print(sum(arrayA))