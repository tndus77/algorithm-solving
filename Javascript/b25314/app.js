const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/b25314/input.txt';
let input = Number(fs.readFileSync(filePath).toString()) / 4;

solution(input);

function solution(input) {
	let long = 'long ';

	console.log(`${long.repeat(input)}int`);
}
