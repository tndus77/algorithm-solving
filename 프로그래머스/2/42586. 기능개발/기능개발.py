def solution(progresses, speeds):
    # 작업 진도 progresses
    # 작업 속도 speeds
    # 조건 1: 뒤에 있는 기능이 먼저 개발되면 앞에 있는 기능이 개발될 때 같이 배포된다.
    # 조건 2: 1일 1배포
    total = []
    answer = []    
    for i in range(len(progresses)):
        rest = 0
        if (100 - progresses[i]) % speeds[i] == 0:
            # 나머지가 없으면
            rest = (100 - progresses[i]) // speeds[i]
        else:
            rest = (100 - progresses[i]) // speeds[i] + 1
        total.append(rest)
    
    pivot = total[0]
    result = 1
    for i in range(1, len(total)):
        if pivot < total[i]:
            answer.append(result)
            pivot = total[i]
            result = 1
        else:
            result += 1
    answer.append(result)
    return answer