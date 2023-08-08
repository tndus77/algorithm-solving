/**
 * sliding Window
 */
const fs = require('fs');
const filePath =
	process.platform === 'linux'
		? '/dev/stdin'
		: 'Javascript/practice/slidingWindow.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

solution(input);

function solution(input) {
	const answerArr = [];
	const [n, k] = input[0].split(' ').map((num) => parseInt(num));
	const arr = input[1].split(' ').map((num) => parseInt(num));
	let sum = 0;
	let left = 0;

	for (left = 0; left < n; left++) {
		if (left + 3 > n) break;
		for (let i = left; i < left + 3; i++) {
			sum += arr[i];
		}
		answerArr.push(sum);
		sum = 0;
	}
	console.log(Math.max(...answerArr));
}

// 선생님 답안
function solution2(k, arr) {
	let answer,
		sum = 0;
	for (let i = 0; i < k; i++) sum += arr[i];
	answer = sum;
	for (let i = k; i < arr.length; i++) {
		sum += arr[i] - arr[i - k];
		answer = Math.max(answer, sum);
	}
	return answer;
}
