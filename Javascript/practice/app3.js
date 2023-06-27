const fs = require('fs');
const filePath =
	process.platform === 'linux'
		? '/dev/stdin'
		: 'Javascript/practice/input3.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

solution(input);

function solution(input) {
	const n = +input[0];
	const arr = [];

	for (let i = 1; i < n; i++) {
		if (i === input.indexOf(input[i])) {
			arr.push(input[i]);
		}
	}
	console.log(arr);
}
