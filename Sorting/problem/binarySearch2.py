#계수 정렬
#모든 원소의 번호를 포함할 수 있는 크기의 리스트를 만든 뒤에
#리스트의 인덱스에 직접 접근하여 특정한 번호의 부품 존재 여부 판단

#n(가게의 부품 개수) 입력받기
n = int(input())
array = [0] * 1000001

#가게의 전체 부품 입력받기
for i in input().split():
    array[int(i)] = 1
    
#m(손님이 요청한 부품의 개수) 입력받기
m = int(input())
search_data = list(map(int, input().split()))

#손님이 확인 요청한 부품 번호를 하나씩 확인
for i in search_data:
    #해당 부품이 존재하는 지
    if array[i] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")
        
#------------
#집합 자료형은 특정한 데이터가 존재하는지 검사할 때 매우 효과적
n = int(input())
#가게에 있는 전체 부품 번호 입력받아 집합(set) 자료형에 기록
array = set(list(map(int, input().split())))

#m 손님이 확인 요청한 부품 개수 입력받기
m = int(input())
x = list(map(int, input().split()))

#손님이 확인 요청한 부품 번호 하나씩 확인
for i in x:
    if i in array:
        print("yes", end=" ")
    else:
        print("no", end=" ")