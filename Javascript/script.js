const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/b1000/text.txt';
let input = fs.readFileSync(filePath).toString().trim();

solution(input);

function solution(input) {}
