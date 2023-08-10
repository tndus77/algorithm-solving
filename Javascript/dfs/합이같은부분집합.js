const fs = require('fs');
const filePath =
	process.platform === 'linux'
		? '/dev/stdin'
		: 'Javascript/dfs/합이같은부분집합.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

solution(input);

function solution(input) {
	let answer = 'NO';
	const arr = input[1].split(',').map((i) => +i);
	const total = arr.reduce((acc, cur) => acc + cur, 0);
	const n = arr.length;
	let flag = false;

	function DFS(L, sum) {
		if (flag) return;
		// L = index, sum = 해당 인덱스를 더해준다.
		if (L === n) {
			// 인덱스가 도달했을 때
			const etc = total - sum; // 반대 부분 집합
			if (etc === sum) {
				answer = 'YES';
				flag = 1;
			} else answer = 'NO';
		} else {
			DFS(L + 1, sum + arr[L]); // o
			DFS(L + 1, sum); // x
		}
	}
	DFS(0, 0);
	console.log(answer);
}
