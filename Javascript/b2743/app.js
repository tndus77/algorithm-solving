const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/b2743/input.txt';
let input = fs.readFileSync(filePath).toString().trim();
solution(input);

function solution(input) {
	console.log(input.length);
}
