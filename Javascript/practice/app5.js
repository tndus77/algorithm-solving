/**
 * 가위바위보
 * A가 이길 경우의 수만 나열
 * 비길 경우 제외하고, 그 외는 모두 B가 이기는 경우
 */
const fs = require('fs');
const filePath =
	process.platform === 'linux'
		? '/dev/stdin'
		: 'Javascript/practice/input5.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

solution(input);

function solution(input) {
	const n = +input[0];
	const firstArr = input[1].split(' ');
	const secondArr = input[2].split(' ');

	for (let i = 0; i < n; i++) {
		if (
			(firstArr[i] === '1' && secondArr[i] === '3') ||
			(firstArr[i] === '2' && secondArr[i] === '1') ||
			(firstArr[i] === '3' && secondArr[i] === '2')
		) {
			console.log('A');
		} else if (firstArr[i] === secondArr[i]) {
			console.log('D');
		} else {
			console.log('B');
		}
	}
}
