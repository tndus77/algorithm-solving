const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/peak/input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

solution(input);

function solution(input) {
	const num = +input[0];
	const arr = input.slice(1).map((item) => item.split(' '));
	let dx = [-1, 0, 1, 0];
	let dy = [0, 1, 0, -1];
	let answer = 0;

	for (let i = 0; i < num; i++) {
		for (let j = 0; j < num; j++) {
			let flag = 1;
			for (let k = 0; k < 4; k++) {
				// 상하좌우 보려고 하는 행 좌표 - 가려고 하는 방향
				let nx = i + dx[k]; // 행
				let ny = j + dy[k]; // 열
				if (
					nx >= 0 &&
					nx < num &&
					ny >= 0 &&
					ny < num &&
					arr[nx][ny] >= arr[i][j]
				) {
					// (nx>=0 && nx<num) && (ny>=0 && ny<n) && 상하좌우 중에 하나라도 크면 봉우리가 아니다.
					flag = 0;
					break;
				}
			}
			if (flag) answer++;
		}
	}
	console.log(answer);
}
