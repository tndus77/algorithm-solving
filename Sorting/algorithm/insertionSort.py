#삽입정렬이 선택정렬보다 효율적이다
#이미 정렬되어 있는 데이터 리스트에서 적절한 위치를 찾는다는 삽입정렬

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    #왼쪽부터 탐색하자!
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]: #내가 왼쪽보다 작다면 
            arr[j], arr[j-1] = arr[j-1], arr[j] #두개 스와프
        else:
            break
            
print(arr)