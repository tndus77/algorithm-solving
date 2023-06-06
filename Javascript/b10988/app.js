/**
 * https://www.acmicpc.net/problem/10988
 */

const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/b10988/input.txt';
let input = fs.readFileSync(filePath).toString().trim();
solution(input);
function solution(input) {
	// 문자열을 배열로 변환 후 다시 문자열로 변환
	if (input.split('').reverse().join('') === input) {
		console.log(1);
	} else {
		console.log(0);
	}
}
