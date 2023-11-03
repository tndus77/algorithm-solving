const fs = require('fs');
const filePath =
	process.platform === 'linux'
		? '/dev/stdin'
		: 'Javascript/softeer/구간합구하기4.txt';
let input = fs.readFileSync(filePath).toString().trim();

solution(input);

function solution(input) {
	const arr = input.split('\n')[1].split(' ').map(Number);
	const sumArr = [0]; // 0부터 시작
	const output = [];

	arr.forEach((v, i) => {
		sumArr[i + 1] = sumArr[i] + v; // sumArr에 arr 값을 하나씩 누적한다
	});
	let calculateArr = input.split('\n').slice(2);
	for (let i = 0; i < calculateArr.length; i++) {
		let [start, end] = calculateArr[i].split(' ');
		output.push(sumArr[end] - sumArr[start - 1]); // output에 push하니까 시간초과 안뜬다
	}

	console.log(output.join('\n'));
}
