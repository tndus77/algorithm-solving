const fs = require('fs');
const filePath =
	process.platform === 'linux'
		? '/dev/stdin'
		: 'Javascript/efficiency/학급회장.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

solution(input);

function solution(input) {
	const n = input[0];
	const arr = input[1].split('');
	const map = new Map();

	for (let i = 0; i < n; i++) {
		if (map.has(arr[i])) {
			map.set(arr[i], map.get(arr[i]) + 1);
		} else {
			map.set(arr[i], 1);
		}
	}

	let max = Number.MIN_SAFE_INTEGER;
	let answer;
	for (let [key, value] of map) {
		if (value > max) {
			max = value;
			answer = key;
		}
	}

	console.log(answer);
}
