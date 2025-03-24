def solution(answers):
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    supo1_cnt, supo2_cnt, supo3_cnt = 0, 0, 0 
    
    for i in range(len(answers)):
        supo1_i, supo2_i, supo3_i = i%len(supo1), i%len(supo2), i%len(supo3)
        if answers[i] == supo1[supo1_i]:
            supo1_cnt += 1
        if answers[i] == supo2[supo2_i]:
            supo2_cnt += 1
        if answers[i] == supo3[supo3_i]:
            supo3_cnt += 1
    
    answer = []
    max_cnt = max(supo1_cnt, supo2_cnt, supo3_cnt)
    if max_cnt == supo1_cnt:
        answer.append(1)
    if max_cnt == supo2_cnt:
        answer.append(2)
    if max_cnt == supo3_cnt:
        answer.append(3)
    
    return answer