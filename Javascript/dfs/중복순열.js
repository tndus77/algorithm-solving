function solution(n, m) {
	const answer = [];
	const temp = Array.from({ length: m }, () => 0);
	// temp[L] = i => 1~n까지의 숫자가 들어가기 때문에

	function DFS(L) {
		if (L === m) {
			answer.push(temp.slice());
		} else {
			// 가지가 뻗어나가야하기 때문에
			for (let i = 1; i <= n; i++) {
				temp[L] = i;
				DFS(L + 1);
			}
		}
	}
	DFS(0);
	return answer;
}

console.log(solution(3, 2));
