#이진 탐색 소스코드 구현 (재귀 함수)
def binary_search(array, target, start, end):
    #배열이
    if start > end:
        return None
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    #중간점의 값보다 찾고자하는 값이 작다면 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    #중간점의 값보다 찾고자 하는 값이 크다면 오른쪽 확인
    else :
        return binary_search(array, target, mid + 1, end)
    
#n(원소의 개수)과 target 값 받기
n, target = list(map(int, input().split()))

#전체 원소 입력받기
array = list(map(int, input().split()))

#이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    #몇 번째 원소인지 출력
    print(result + 1)
    
#---------------
def binary_search(array, target, start, end):
    while(start <= end):
        mid = (start + end) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else :
            start = mid + 1
    return None

