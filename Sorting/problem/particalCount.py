#정렬된 배열에서 특정 수의 개수 구하기
from bisect import bisect_left, bisect_right

#데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = list(map(int, input().split())) #n은 원소의 개수, x는 특정 숫자
array = list(map(int, input().split()))

#값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)