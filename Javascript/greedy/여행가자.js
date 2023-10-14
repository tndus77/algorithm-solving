/**
 * 한 번 방문했던 도시들을 여러 번 방문해도 상관없으니 유니온 파인드로 풀어도 된다.
 */
const fs = require('fs');
const filePath =
	process.platform === 'linux'
		? '/dev/stdin'
		: 'Javascript/greedy/여행가자.txt';
let input = fs.readFileSync(filePath).toString().trim().split('\n');

solution(input);

function solution(input) {
	let n = Number(input[0]);
	let m = Number(input[1]);
	const arr = input.slice(2, n + 2).map((i) => i.split(' '));
	const lastArr = input.slice(n + 2).map((i) => i.split(' '));

	let parent = [];
	// 초기화
	for (let i = 0; i < n; i++) {
		parent.push(i);
	}

	// 두 도시가 연결되어 있다면
	for (let i = 0; i < n; i++) {
		for (let j = i + 1; j < n; j++) {
			if (parent[i][j] === 1) union(i, j);
		}
	}

	// 여행 경로가 동일한 root를 가지는지
	for (let i = 1; i <= m; i++) {
		let a = find(lastArr[i - 1]);
		let b = find(lastArr[i + 1]);
		if (a !== b) {
			console.log('No');
			return;
		}
	}
	console.log('YES');

	function find(x) {
		if (parent[x] === x) return x;
		else return find(parent[x]);
	}

	function union(x, y) {
		let a = find(x);
		let b = find(y);

		if (a === b) return -1;
		else {
			if (a > b) {
				parent[a] = b;
			} else {
				parent[b] = a;
			}
		}
		return e[2];
	}
}
