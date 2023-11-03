const fs = require('fs');
const filePath =
	process.platform === 'linux' ? '/dev/stdin' : 'Javascript/softeer/블로그.txt';
let input = fs.readFileSync(filePath).toString().trim().split('\n');

solution(input);
/**
 *
 * @param {} input
 * 슬라이딩 윈도우 알고리즘 => 왼쪽 빼고 오른쪽 추가
 * n - x + 1: 최대 방문자 수를 찾을 수 있는 유효한 시작 지점의 개수
 */
function solution(input) {
	const [n, x] = input[0].split(' ').map(Number);
	const arr = input[1].split(' ').map(Number);

	let curV = 0; // 현재 값
	let maxV = 0; // 최대 값
	let maxC = 0; // 기간 count
	for (let i = 0; i < n - x + 1; i++) {
		// default 값
		if (i === 0) {
			for (let j = 0; j < x; j++) {
				curV += arr[j];
			}
			maxV = curV;
			maxC = 1;
		} else {
			// 왼쪽 빼고 오른쪽 추가
			curV = curV - arr[i - 1] + arr[i + x - 1];
			if (curV === maxV) {
				maxC++;
			} else if (curV > maxV) {
				maxV = curV;
				maxC = 1; // 다시 maxC 재정리 = 다른 값으로 바꼈으니까
			}
		}
	}
	if (maxV === 0) return console.log('SAD');
	else return console.log(`${maxV}\n${maxC}`);
}
