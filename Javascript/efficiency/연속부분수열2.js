/**
 * 포문을 돌려주면서 sum에 값을 더해주고
 * sum이 M보다 크면 조건에 어긋나므로 start 포인터를 증가시켜주고
 * sum에서 arr[start] 값을 빼준다.
 * 조건에 맞다면 연속부분수열이므로 마지막 인덱스 - 시작 인덱스 + 1을 하면 총 갯수가 나온다.
 */
const fs = require('fs');
const filePath =
	process.platform === 'linux'
		? '/dev/stdin'
		: 'Javascript/efficiency/연속부분수열2.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

solution(input);

function solution(input) {
	const [N, M] = input[0].split(' ').map((num) => parseInt(num));
	const arr = input[1].split(' ').map((num) => parseInt(num));
	let sum = 0; // 합계
	let answer = 0; // 정답
	let start = 0; // 시작 포인터

	for (let end = 0; end < N; end++) {
		sum += arr[end];
		while (sum > M) {
			sum -= arr[start++];
		}
		answer += end - start + 1;
	}
	console.log(answer);
}
