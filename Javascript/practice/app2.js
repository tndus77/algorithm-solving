const fs = require('fs');
const filePath =
	process.platform === 'linux'
		? '/dev/stdin'
		: 'Javascript/practice/input2.txt';
const input = fs.readFileSync(filePath).toString().trim();

solution(input);

function solution(input) {
	const arr = input.split('');
	let answer = '';
	for (let i = 0; i < arr.length; i++) {
		if (i === arr.indexOf(arr[i])) {
			answer += arr[i];
		}
	}
	console.log(answer);
}
