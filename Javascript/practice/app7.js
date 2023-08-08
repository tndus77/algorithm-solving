const fs = require('fs');
const filePath =
	process.platform === 'linux'
		? '/dev/stdin'
		: 'Javascript/practice/input7.txt';
const input = fs.readFileSync(filePath).toString().split(' ');

solution(input);

function solution(input) {
	const arr = input[0].split('');
	const idxArr = Array.from({ length: arr.length }, () => 0);
	console.log(idxArr);
	let P = 1000;
	// 돌면서 인덱스 비교 (단. Math.min 사용해서 최소값으로 구하기)
	for (let i = 0; i < arr.length; i++) {
		// 왼쪽에 있는 e로부터 떨어져있는 숫자
		if (arr[i] === 'e') {
			P = 0;
		}
		P += 1;
	}
}
