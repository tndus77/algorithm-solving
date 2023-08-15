function solution(n, m) {
	let answer = [];
	const temp = Array.from({ length: m }, () => 0);
	function DFS(L, s) {
		if (L === m) {
			// level이 m가 같게 되면 (마지막까지 뽑은 것이기 때문에) return
			answer.push(temp.slice());
		} else {
			for (let i = s; i <= n; i++) {
				temp[L] = i;
				DFS(L + 1, i + 1);
			}
		}
	}
	DFS(0, 1);
	return answer;
}

console.log(solution(4, 2)); // 4개 중 2개를 뽑는다.
