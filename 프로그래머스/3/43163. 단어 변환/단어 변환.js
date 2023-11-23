function solution(begin, target, words) {
    const visited = {[begin]: 0};
    const queue = [begin];
    
    function isConnected(str1, str2) {
        let count = 0;
           for(let i=0; i<str1.length; i++) {
            if (str1[i] !== str2[i]) count++;
        }
        
        return count === 1 ? true: false;
    }
    
    while(queue.length) {
        let cur = queue.shift();
        
        if (cur === target) break;
        for (const word of words) {
            if (isConnected(word, cur) && !visited[word]) {
                visited[word] = visited[cur] + 1;
                queue.push(word)
            }
        }
    }
    return visited[target] ?? 0
}
