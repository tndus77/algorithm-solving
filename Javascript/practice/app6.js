const fs = require('fs');
const filePath =
	process.platform === 'linux'
		? '/dev/stdin'
		: 'Javascript/practice/input6.txt';
const input = fs.readFileSync(filePath).toString().trim().split('');

solution(input);

function solution(input) {
	for (let i = 0; i < input.length - 1; i++) {
		if (input[i] === input[i].toLowerCase()) {
			input[i] = input[i].toUpperCase();
		}
	}
	console.log(input.join(''));
}
