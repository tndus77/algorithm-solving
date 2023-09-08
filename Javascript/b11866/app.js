const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/b11866/text.txt';
const input = fs.readFileSync(filePath).toString().trim();

solution(input);

function solution(input) {
	const n = input.split(' ')[0];
	const k = input.split(' ')[1];
	const queue = [];
	const answer = [];

	for (let i = 1; i <= n; i++) {
		queue.push(i);
	}

	let count = 1;
	while (queue.length) {
		if (count % k === 0) {
			answer.push(queue.shift());
		} else queue.push(queue.shift());
		count++;
	}

	console.log(`<${answer.join(', ')}>`);
}
