const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/b1157/text.txt';
const input = fs.readFileSync(filePath).toString();

solution(input);
function solution(input) {
	const map = new Map();
	const str = input.toUpperCase();

	for (const x of str) {
		map.set(x, (map.get(x) || 0) + 1);
	}

	let maxFrequency = 0; // 가장 많이 나타난 알파벳의 빈도수
	let mostFrequentLetters = []; // 가장 많이 나타난 알파벳들

	for (const [key, value] of map) {
		if (value > maxFrequency) {
			// 현재 알파벳의 빈도수가 최대 빈도수보다 큰 경우
			maxFrequency = value;
			mostFrequentLetters = [key]; // 새로운 최다빈도 알파벳을 배열에 저장
			console.log('mostFrequentLetters', mostFrequentLetters);
		} else if (value === maxFrequency) {
			// 현재 알파벳의 빈도수가 최대 빈도수와 같은 경우
			mostFrequentLetters.push(key); // 배열에 추가
		}
	}

	if (mostFrequentLetters.length > 1) {
		console.log('?'); // 최다빈도 알파벳이 여러 개인 경우
	} else {
		console.log(mostFrequentLetters[0]); // 가장 많이 나타난 알파벳 출력
	}
}
