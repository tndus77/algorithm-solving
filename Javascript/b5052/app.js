/**
 * https://www.acmicpc.net/problem/5052
 */
const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/b5052/input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

solution(input);

function solution(input) {
	let idx = 0;
	let number = +input[idx++];

	while (number--) {
		let n = +input[idx++];
		let arr = Array.from({ length: n }, () => input[idx++]).sort(); // 새 배열을 만들고 idx를 늘려가는 방식이 새롭다..!

		let flag = 'YES';

		for (let i = 0; i < n; i++) {
			if (arr[i].slice(0, arr[i].length).startsWith(arr[i - 1])) {
				flag = 'NO';
				break;
			}
		}
		console.log(flag);
	}
}
