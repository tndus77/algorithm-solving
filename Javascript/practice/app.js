const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/practice/input.txt';
const input = fs.readFileSync(filePath).toString().trim();

solution(input);

function solution(input) {
	const arr = input.split('');
	for (let i = 0; i < arr.length; i++) {
		if (arr[i] === 'A') {
			arr[i] = '#';
		}
	}
	console.log(arr.join(''));
}
