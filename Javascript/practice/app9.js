const fs = require('fs');
const filePath =
	process.platform === 'linux'
		? '/dev/stdin'
		: 'Javascript/practice/input9.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

solution(input);

function solution(input) {
	const arr = [];
	let answer = 0;
	for (let i = 0; i < input.length; i++) {
		arr.push(input[i].split(' '));
	}

	for (let i = 1; i <= arr[0].length; i++) {
		for (let j = 1; j <= arr[0].length; j++) {
			let cnt = 0;
			for (let k = 0; k < arr.length; k++) {
				let pi = 0;
				let pj = 0;
				for (let s = 0; s < arr[0].length; s++) {
					if (arr[k][s] === i) pi = s;
					if (arr[k][s] === j) pj = s;
				}
				if (pi < pj) cnt++;
			}
			if (cnt === arr.length) answer++;
		}
	}
	console.log(answer);
}
