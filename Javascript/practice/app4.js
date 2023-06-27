const fs = require('fs');
const filePath =
	process.platform === 'linux'
		? '/dev/stdin'
		: 'Javascript/practice/input4.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

solution(input);

function solution(input) {
	const n = +input[0];
	const arr = input[1].split(' ');
	let max = arr[0];
	let count = 1; // 첫번째는 무조건 포함
	for (let i = 0; i < n; i++) {
		if (arr[i] > max) {
			max = arr[i];
			count += 1;
		}
	}
	console.log(count);
}
