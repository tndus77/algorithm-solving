/**
 *
 * @param {*} s 현수 위치
 * @param {*} e 송아지 위치
 * @returns 점프의 최소 횟수
 */
function solution(s, e) {
	const ch = Array.from({ length: 10001 }, () => 0);
	const dis = Array.from({ length: 10001 }, () => 0);
	const queue = [];
	ch[s] = 1;
	queue.push(s);

	while (queue.length) {
		// 부모 노드 하나 빼기. 현수 위치
		const v = queue.shift();
		for (nv of [v - 1, v + 1, v + 5]) {
			dis[nv] = dis[v] + 1; // 부모 노드의 거리 + 1
			if (nv === e) return dis[nv];
			if (nv > 0 && nv <= 1000 && ch[nv] !== 1) {
				ch[nv] = 1;
				queue.push(nv);
			}
		}
	}

	return answer;
}

console.log(solution(8, 3));
