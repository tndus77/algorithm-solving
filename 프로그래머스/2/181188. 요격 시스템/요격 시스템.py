def solution(targets):
    answer = 0
    # 정렬
    # 현재 끝점과 다음 시작점 비교, 이전이면 포함 & 다음 것도 비교, 아니면 미포함(answer+= 1) & 다음 행으로 넘어간다.
    targets.sort(key = lambda x:x[1])
    end = 0
    for s, e in targets:
        if s >= end:
            answer += 1
            end = e
    return answer