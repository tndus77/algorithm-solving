const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/b3003/input.txt';
let input = fs.readFileSync(filePath).toString().trim().split(' ');
solution(input);

function solution(input) {
	let chess = [1, 1, 2, 2, 2, 8];
	let inputArr = input.map((item) => +item); // number[]로 변환
	let result = chess.map((item, index) => item - inputArr[index]);
	console.log(result.join(' '));
}
