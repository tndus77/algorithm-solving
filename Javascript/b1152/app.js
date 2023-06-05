const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/b1152/input.txt';
let input = fs.readFileSync(filePath).toString().trim().split(' ');

solution(input);

function solution(input) {
	console.log(input[0] === '' ? 0 : input.length);
}
