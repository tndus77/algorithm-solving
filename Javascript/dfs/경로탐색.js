/**
 *
 * @param n 정점의 수
 * @param arr 배열
 */
function solution(n, arr) {
	const graph = Array.from(Array(n + 1), () => Array(n + 1).fill(0));
	const ch = Array.from({ length: n + 1 }, () => 0);
	let answer = 0;
	for (let [a, b] of arr) {
		graph[a][b] = 1; // 방향 그래프이기 때문에 graph[a][b]만 1로 설정. 무방향이면 graph[b][a]=1도 설정해야 함.
	}
	function DFS(v) {
		if (v === n) {
			answer++;
		} else {
			for (let i = 1; i <= n; i++) {
				if (graph[v][i] === 1 && ch[i] === 0) {
					// 정점 v에서 i로 갈 수 있고, 방문하지 않았다면
					ch[i] = 1;
					DFS(i);
					// back
					ch[i] = 0;
				}
			}
		}
	}
	ch[1] = 1;
	DFS(1);
	return answer;
}

let arr = [
	[1, 2],
	[1, 3],
	[1, 4],
	[2, 1],
	[2, 3],
	[2, 5],
	[3, 4],
	[4, 2],
	[4, 5],
];
console.log(solution(5, arr));
