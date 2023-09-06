const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/b1205/input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

solution(input);

function solution(input) {
	const num = +input[0];

	const scoreArr = +input[1].split(' ').map((item) => +item);
	const rankArr = Array.from({ length: num }, () => 1);
	console.log(scoreArr);
	console.log(rankArr);

	for (let i = 0; i < num; i++) {
		for (let j = 0; j < num; j++) {
			if (scoreArr[i] < scoreArr[j]) {
				rankArr[i]++;
			}
		}
	}
	console.log(rankArr);
}
