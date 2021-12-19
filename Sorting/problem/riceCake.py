#떡의 개수n과 요청한 떡의 길이 m
n, m = list(map(int, input().split()))
#떡의 개별 높이 
array = list(map(int, input().split()))

#이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array) #가장 긴 떡의 길이

while(start <= end):
    total = 0
    mid = (start+end)//2
    for x in array: #현재의 높이로 떡을 자랐을 때 
        if x > mid: #현재의 떡의 길이가 높이보다 높아야 얻을 수 있으므로
            total += x - mid
    #떡의 양의 부족한 경우 더 많이 자르기 위해 왼쪽으로 이동
    if total < m:
        end = mid - 1
        
    else:
        result = mid #최대한 덜 잘랐을 때가 정답
        
print(result)
        start = mid + 1