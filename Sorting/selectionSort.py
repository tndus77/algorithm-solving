#10개의 데이터
#가장 작은 데이터를 선택에 맨 앞에 놓고
#그 다음 작은 데이터를 두 번째 데이터와 바꿔야 한다

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    
for i in range(len(array)):
    #가장 작은 값 인덱스와 차례대로 가는 j의 필요성
    min_index = i
    for j in range(i+1, len(array)):
    #가장 작은 데이터 구하기 
        if array[min_index] > array[j] :
            min_index = j   
    #스와프
    array[i], array[min_index] = array[min_index], array[i]
    