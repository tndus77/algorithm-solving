const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/b1158/test.txt';
let input = fs.readFileSync(filePath).toString().trim();

solution(input);

function solution(input) {
	const [n, k] = input.split(' ');
	const queue = [];
	const answer = [];

	for (let i = 0; i < n; i++) {
		queue.push(i + 1);
	}

	while (queue.length) {
		const removeItem = queue.shift();
		if (removeItem % k === 0) answer.push(removeItem);
		else queue.push(removeItem);
	}
	console.log(`<${answer.join(', ')}>`);
}
