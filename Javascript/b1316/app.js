/**
 * 풀이
 * https://new-anecdote.tistory.com/15
 */
const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/b1316/input.txt';
let input = fs.readFileSync(filePath).toString().trim().split('\n');

solution(input);

function solution(input) {
	let count = 0;
	for (let i = 1; i < input.length; i++) {
		const str = input[i].split('');
		if (isGroup(str).join('') === str.join('')) {
			count++;
		}
	}
	console.log(count);

	/** 그룹 판단 함수 */
	function isGroup(str) {
		let newArr = [];
		for (let i = 0; i < str.length; i++) {
			// 배열 안에 아무것도 없거나 이전 값과 현재 값이 같으면
			if (newArr.indexOf(str[i]) === -1 || str[i] === str[i - 1]) {
				newArr.push(str[i]);
			}
		}
		return newArr;
	}
}
