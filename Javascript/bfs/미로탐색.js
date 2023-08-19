function solution(board) {
	let answer = 0;
	const dx = [-1, 0, 1, 0];
	const dy = [0, 1, 0, -1];

	function BFS(x, y) {
		// x 행, y 열
		if (x === 6 && y === 6) answer++;
		else {
			for (let k = 0; k < 4; k++) {
				let nx = x + dx[k];
				let ny = y + dy[k];
				if (nx >= 0 && nx <= 6 && ny >= 0 && ny <= 6 && board[nx][ny] === 0) {
					// board[nx][ny] === 0 => 통로인 곳
					board[nx][ny] = 1; // 방문 처리
					BFS(nx, ny);
					board[nx][ny] = 0;
				}
			}
		}
	}
	board[0][0] = 1;
	BFS(0, 0);
	return answer;
}

let arr = [
	[0, 0, 0, 0, 0, 0, 0],
	[0, 1, 1, 1, 1, 1, 0],
	[0, 0, 0, 1, 0, 0, 0],
	[1, 1, 0, 1, 0, 1, 1],
	[1, 1, 0, 0, 0, 0, 1],
	[1, 1, 0, 1, 1, 0, 0],
	[1, 0, 0, 0, 0, 0, 0],
];

console.log(solution(arr));
