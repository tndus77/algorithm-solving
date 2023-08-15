function solution(input) {
	let answer = 1;
	function DFS(n) {
		if (n < 1) return 1;
		else return n * DFS(n - 1);
	}
	answer = DFS(input);
	return answer;
}

console.log(solution(4));
