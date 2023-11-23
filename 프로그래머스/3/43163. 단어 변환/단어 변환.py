from collections import deque

def solution(begin, target, words):
    queue = deque()
    queue.append([begin, 0])
    
    if target not in words:
        return 0
    
    while queue:
        cur, step = queue.popleft()
        if cur == target:
            return step

        for word in words:
            cnt = 0
            for i in range(len(word)):
                if cur[i] != word[i]:
                    cnt += 1
            if cnt == 1:
                queue.append([word, step + 1])
    return queue[target]