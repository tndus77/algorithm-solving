function solution(targets) {
    let answer = 0;
    
    targets.sort((a, b) => a[1]-b[1])
    
    let end = 0
    for (let i = 0; i<targets.length; i++) {
        [s, e] = targets[i]
        
        if (s >= end) {
            end = e
            answer += 1   
        }
    }
    return answer;
}