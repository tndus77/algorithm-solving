/**
 * 이번 정보 올림피아드대회에서 좋은 성적을 내기 위하여 현수는 선생님이 주신 N개의 문제를 풀려고 한다.
 * 각 문제는 그것을 풀었을 때 얻는 점수와 푸는 데 걸리는 시간이 주어지게 된다.
 * 제한 시간 M 안에 N개의 문제 중 최대점수를 얻을 수 있는 경우를 구하는 문제이다.
 * 단, 해당 문제는 해당 시간이 걸리면 푸는 걸로 간주하고 한 유형당 한 개만 풀 수 있다.
 */
const fs = require('fs');
const filePath =
	process.platform === 'linux'
		? '/dev/stdin'
		: 'Javascript/dfs/최대점수구하기.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

solution(input);

function solution(input) {
	const [n, m] = input[0].split(' ').map((i) => +i);
	let answer = Number.MIN_SAFE_INTEGER;
	const ps = []; // 점수
	const pt = []; // 문제를 푸는데 걸리는 시간
	for (let i = 1; i < n; i++) {
		[ps[i], pt[i]] = input[i].split(' ').map((i) => +i);
	}

	function DFS(L, sum, time) {
		if (time > m) return;
		if (L === n) {
			if (time <= m) {
				answer = Math.max(answer, sum);
			}
		} else {
			DFS(L + 1, sum + ps[L], time + pt[L]); // 문제를 푼다
			DFS(L + 1, sum, time); // 문제를 안푼다
		}
	}

	DFS(0, 0, 0);
	console.log(answer);
}
