const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/b3151/input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

solution(input);

function solution(input) {
	const n = input[0];
	const arr = input[1]
		.split(' ')
		.map((i) => +i)
		.sort((a, b) => a - b);
	let answer = 0;

	// 합이 0보다 작으면 left ++
	// 합이 0보다 크면 right ++
	// i는 하나의 요소 기준
	for (let i = 0; i < n - 2; i++) {
		let left = i + 1;
		let right = n - 1;

		while (left < right) {
			const sum = arr[i] + arr[left] + arr[right];
			if (sum === 0) {
				answer++;
				left++;
				right--;
			} else if (sum < 0) {
				left++;
			} else {
				right--;
			}
		}
	}
	console.log('answer', answer);
}
