const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/b2506/input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

console.log(solution(input));

function solution(input) {
	const num = +input[0];

	const arr = input[1].split(' ');

	let cnt = 0;
	let answer = 0;

	for (let i = 0; i < num; i++) {
		if (Number(arr[i]) === 1) {
			cnt++;
			answer += cnt;
		} else cnt = 0;
	}
	return answer;
}
