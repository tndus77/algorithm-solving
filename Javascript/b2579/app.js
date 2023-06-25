const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/b2579/input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

solution(input);

function solution(input) {
	let answer = 0;
	// 점화식을 만든다.
	// dy 자체도 배열로 만든다. Array.from({길이}, () => 0) 0으로 초기화
	const dy = Array.from({ length: input.length + 1 }, () => 0);
	dy[1] = 1;
	dy[2] = 2;

	for (let i = 3; i <= input.length; i++) {
		dy[i] = dy[i - 2] + dy[i - 1];
	}

	answer = dy[input.length];
	console.log(answer);
	return answer;
}
