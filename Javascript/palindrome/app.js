const fs = require('fs');
const filePath =
	process.platform === 'linux'
		? '/dev/stdin'
		: 'Javascript/palindrome/input.txt';
const input = fs.readFileSync(filePath).toString();

solution(input);

function solution(input) {
	let answer = 'YES';
	// 정규식 (replace) 사용해서 알파벳이 아닌 것들 삭제
	input = input.toLowerCase().replace(/[^a-z]/g, '');
	if (input.split('').reverse().join('') !== input) return 'NO';

	console.log(answer);
}
