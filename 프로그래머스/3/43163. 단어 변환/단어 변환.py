from collections import deque

def can_convert(w1, w2):
    diff = 0
    for a, b in zip(w1, w2):
        if a != b:
            diff += 1
        if diff > 1:
            return False
    return diff == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = set()
    q = deque([(begin, 0)])
    
    while q:
        current, depth = q.popleft()
        
        if current == target:
            return depth
        
        for word in words:
            if word not in visited and can_convert(current, word):
                visited.add(word)
                q.append((word, depth+1))
    return 0