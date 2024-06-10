def solution(sequence, k):
   # L과 R로 접근하는 문제
    L = R = 0
    answer = [0, len(sequence)]
    
    total = sequence[0]
    while True:
        if total < k: # 오른쪽 ++
            R += 1
            if R == len(sequence):
                break
            total += sequence[R]
        else:
            if total == k:
                if answer[1] - answer[0] > R - L:
                    answer = [L, R]
            total -= sequence[L]
            L += 1
    return answer
        