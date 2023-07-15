const fs = require('fs');
const filePath =
	process.platform === 'linux'
		? '/dev/stdin'
		: 'Javascript/practice/input8.txt';
const input = fs.readFileSync(filePath).toString().split('');

solution(input);

function solution(input) {
	let count = 1;
	let answer = '';
	for (let i = 0; i < input.length; i++) {
		if (input[i] === input[i + 1]) {
			count++;
		} else {
			answer += input[i];
			if (count > 1) answer += String(count);
			count = 1;
		}
	}
	console.log(answer);
}
