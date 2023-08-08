const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/onlyNum/input.txt';
const input = fs.readFileSync(filePath).toString().split('');

solution(input);

function solution(input) {
	let answer = '';
	// // 정규식 (replace) 사용해서 숫자가 아닌 것들 삭제
	// input = input.replace(/['^a-zA-Z']/g, '');
	// console.log(input);

	for (let x of input) {
		if (!isNaN(x)) answer += x;
	}
	console.log(parseInt(answer));
}
