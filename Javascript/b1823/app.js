const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/b1823/input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

solution(input);

function solution(input) {
	const n = +input[0];
	let maxProfit = 0;

	for (let i = 0; i < n; i++) {
		const profit = input[i + 1] * (i + 1);
		maxProfit += profit;
	}

	console.log(maxProfit);
}
