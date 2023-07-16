/**
 * 이중 for문으로 돌면 시간초과
 * 투포인터는 O(n)으로 해결 가능
 */
const fs = require('fs');
const filePath =
	process.platform === 'linux'
		? '/dev/stdin'
		: 'Javascript/efficiency/연속부분수열.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

solution(input);

function solution(input) {
	// left, right가 있음 => 투 포인터
	// sum < m => right++ -> sum += arr[right]
	// sum > m => left++ -> sum -= arr[left]
	const [n, m] = input[0].split(' ').map((i) => +i);
	const arr = input[1].split(' ').map((i) => +i);
	let sum = 0;
	let left = 0;
	let answer = 0;
	for (let right = 0; right < n; right++) {
		sum += arr[right];
		if (sum === m) answer++;
		while (sum > m) {
			// sum > m
			sum -= arr[left++];
			if (sum === m) answer++;
		}
	}
	console.log(answer);
}
