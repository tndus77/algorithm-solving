const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/b1834/text.txt';
let input = fs.readFileSync(filePath).toString().trim();

solution(input);

function solution(input) {
	let count = 0;
	for (let i = 1; i < input; i++) {
		count += (Number(input) + 1) * i;
	}
	console.log(count);
}
