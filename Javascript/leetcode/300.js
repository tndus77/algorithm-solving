/**
 *
 */
const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/leetcode/300.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

/**
 * 최대부분증가수열 (LTS)
 * dy에 누적된 값을 더한다.
 * dy[i]는 i번째 인덱스까지의 증가하는 부분수열의 최대 길이를 저장한다.
 * arr[i]일 때 arr[0] ~ arr[j = i-1]까지 돈다.
 * 만약 arr[i] > arr[j]이면 dy에서 가장 큰 값을 찾아서 +1을 해준다.
 * 없으면 그냥 dy[i] = 1이다.
 * dy에서 최대 값을 출력한다.
 */

solution(input);

function solution(input) {
	const arr = input[1].split(' ').map((num) => parseInt(num));
	const dy = Array.from({ length: input[0] }, () => 0);
	let answer = 0;

	for (let i = 0; i < arr.length; i++) {
		let max = 0;
		for (let j = i - 1; j >= 0; j--) {
			if (arr[i] > arr[j] && dy[j] > max) {
				max = dy[j];
			}
			dy[i] = max + 1;
		}
		answer = Math.max(answer, dy[i]); // 최대값을 지속적으로 저장한다.
	}
	console.log(answer);
}
