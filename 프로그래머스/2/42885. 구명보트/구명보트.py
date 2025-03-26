def solution(people, limit):
    answer = 0
    people.sort()
    left, right = 0, len(people) - 1
    
    while left <= right:
        if people[left] + people[right] <= limit:
            # 가장 가벼운 사람과 무거운 사람을 태울 수 있으면
            left += 1
        # 무거운 사람은 항상 태운다
        right -= 1
        answer += 1
    return answer