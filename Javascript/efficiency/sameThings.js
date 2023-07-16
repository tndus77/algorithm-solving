const fs = require('fs');
const filePath =
	process.platform === 'linux'
		? '/dev/stdin'
		: 'Javascript/efficiency/sameThings.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

solution(input);

function solution(input) {
	const arr1 = input[1]
		.split(' ')
		.map((item) => +item)
		.sort();
	const arr2 = input[3]
		.split(' ')
		.map((item) => +item)
		.sort();
	const n = arr1.length;
	const m = arr2.length;
	let p1 = 0;
	let p2 = 0;
	const answer = [];

	while (p1 < n && p2 < m) {
		// 같으면 answer 배열에 넣고, 두 포인터 모두 증가
		// arr1[p1] < arr2[p2] 이면 p1만 증가
		// arr1[p1] > arr2[p2] 이면 p2만 증가
		if (arr1[p1] === arr2[p2]) {
			answer.push(arr1[p1++]);
			p2++;
		} else if (arr1[p1] < arr2[p2]) {
			p1++;
		} else if (arr1[p1] > arr2[p2]) {
			p2++;
		}
	}
	console.log(answer);
}
