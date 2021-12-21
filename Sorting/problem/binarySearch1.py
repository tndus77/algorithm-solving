def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
array = list(map(int, input().split()))
    
array.sort()

m = int(input())
search_data = list(map(int, input().split()))
    
for x in search_data:
    result = binary_search(array, x, 0, n-1)
    if result != None:
        print("yes", end=" ")
    else:
        print("no", end=" ")