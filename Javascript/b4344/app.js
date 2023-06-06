/**
 * https://www.acmicpc.net/problem/4344
 */

const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/b4344/input.txt';
let input = fs.readFileSync(filePath).toString().trim().split('\n');

solution(input);

function solution(input) {
	for (let i = 1; i <= input[0]; i++) {
		const arr = input[i].split(' ').map((item) => +item);
		let sum = 0;
		for (let i = 1; i < arr.length; i++) {
			sum += arr[i];
		}
		// 평균
		const result = sum / arr[0];

		// 전체 인원과 평균 이상의 학생 수 비교
		let count = 0;
		for (let i = 1; i < arr.length; i++) {
			if (arr[i] > result) {
				count += 1;
			}
		}
		const answer = (count / arr[0]) * 100;
		console.log(answer.toFixed(3) + '%');
	}
}
