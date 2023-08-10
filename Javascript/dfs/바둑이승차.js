const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/dfs/바둑이승차.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

solution(input);

function solution(input) {
	const [limit, n] = input[0].split(' ').map((i) => +i);
	const arr = input.slice(1).map((i) => +i);
	let answer = Number.MIN_SAFE_INTEGER;

	function DFS(L, sum) {
		if (sum > limit) return;
		if (L === arr.length) {
			if (sum <= limit) {
				// 바둑이는 limit을 넘을 수 없다.
				answer = Math.max(answer, sum);
			}
		} else {
			DFS(L + 1, sum + arr[L]);
			DFS(L + 1, sum);
		}
	}
	DFS(0, 0);
	console.log(answer);
}
