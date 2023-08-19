/**
 * 넓이 우선 탐색
 * queque를 이용하여 구현
 *
 * - 로직
 * 1. 처음 수 넣고, 그 수와 연결된 수를 queque에 넣는다.
 * 2. queque에서 하나씩 빼면서 그 수와 연결된 수를 queque에 넣는다.
 */

function solution() {
	let answer = '';
	const queue = [];
	queue.push(1);
	while (queue.length) {
		let v = queue.shift();
		answer += v + ' ';

		for (let nv of [v * 2, v * 2 + 1]) {
			if (nv > 7) continue;
			queue.push(nv);
		}
	}
	return answer;
}

console.log(solution());
