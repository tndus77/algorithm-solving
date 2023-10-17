function solution(k, dungeons) {
    let answer = 0;
    let result = [];
    let visited = Array.from({length: dungeons.length}, () => false)
    
    const DFS = (count, k) => {
        result.push(count);
        
        for (let i=0; i<dungeons.length; i++) {
            const [cur, need] = dungeons[i];
            if (k >= cur && !visited[i]) {
                visited[i] = 1;
                DFS(count + 1, k - need);
                visited[i] = 0;
            }
        }   
    }
    DFS(0, k)
    answer = Math.max(...result)
    return answer;
}