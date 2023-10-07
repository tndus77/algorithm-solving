function solution(n, computers) {
	let answer = 0;
	let nn = computers.length;
	let m = computers[0].length;
	let visited = Array.from({ length: n }, () => false);

	function DFS(x) {
		visited[x] = true;

		for (let i = 0; i < m; i++) {
			if (computers[x][i] === 1 && !visited[i]) {
				DFS(i);
			}
		}
	}

	for (let i = 0; i < nn; i++) {
		if (!visited[i]) {
			DFS(i);
			answer += 1;
		}
	}
	return answer;
}
