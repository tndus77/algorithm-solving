/**
 * 두 배열 합치기
 * 오름차순으로 정렬이 된 두 배열이 주어지면 두 배열을 오름차순으로 합쳐 출력
 */
const fs = require('fs');
const filePath =
	process.platform === 'linux'
		? '/dev/stdin'
		: 'Javascript/efficiency/twoPointers.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

solution(input);

function solution(input) {
	const answer = [];
	const arr1 = input[1].split(' ').map((item) => +item);
	const arr2 = input[3].split(' ').map((item) => +item);
	let n = arr1.length;
	let m = arr2.length;
	let p1 = (p2 = 0);
	while (p1 < n && p2 < m) {
		if (arr1[p1] <= arr2[p2]) {
			answer.push(arr1[p1++]);
		} else answer.push(arr2[p2++]);
	}
	while (p1 < n) answer.push(arr1[p1++]);
	while (p2 < m) answer.push(arr2[p2++]);
	console.log(answer);
	// 투포인터 알고리즘 -> 하나의 배열 당 하나의 포인터
	// 각각의 배열을 두고, p1과 p2 중 값을 비교 후 작은 값을 answer에 넣어준다
}
