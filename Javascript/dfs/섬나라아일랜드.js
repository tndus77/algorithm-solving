function solution(board) {
	let dx = [-1, -1, 0, 1, 1, 1, 0, -1];
	let dy = [0, 1, 1, 1, 0, -1, -1, -1];
	let n = board.length;
	let answer = 0;

	function DFS(x, y) {
		// 8 방향 탐색
		for (let k = 0; k < 8; k++) {
			let nx = x + dx[k];
			let ny = y + dy[k];
			if (nx >= 0 && ny >= 0 && nx < n && ny < n && board[nx][ny] === 1) {
				board[nx][ny] = 0;
				DFS(nx, ny);
			}
		}
	}

	for (let i = 0; i < n; i++) {
		for (let j = 0; j < n; j++) {
			if (board[i][j] === 1) {
				board[i][j] = 0;
				answer++;
				DFS(i, j);
			}
		}
	}

	return answer;
}

let arr = [
	[1, 1, 0, 0, 0, 1, 0],
	[0, 1, 1, 0, 1, 1, 0],
	[0, 1, 0, 0, 0, 0, 0],
	[0, 0, 0, 1, 0, 1, 1],
	[1, 1, 0, 1, 1, 0, 0],
	[1, 0, 0, 0, 1, 0, 0],
	[1, 0, 1, 0, 1, 0, 0],
];
console.log(solution(arr));
