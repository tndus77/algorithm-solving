const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/b10797/text.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

solution(input);

function solution(input) {
	const n = input[0];
	const arr = input[1].split(' ').map((i) => +i);
	let flag = false;

	const hashMap = new Map();
	for (const x of arr) {
		hashMap.set(x, (hashMap.get(x) || 0) + 1);
	}

	for (const i of hashMap) {
		if (Number(i[0]) === Number(n)) {
			flag = true;
			console.log(i[1]);
		}
	}

	if (!flag) console.log(0);
}
