/**
 *
 * @param {} arr
 * 1. 방문하지 않고 0 일 경우 방문 처리
 * 2. 방문한 지점에서 상, 하, 좌, 우 살펴보고 방문 처리 과정을 하면 모든 지점을 방문할 수 있음
 * 3. 모든 노드에 대하여 1~2번을 진행하고, 방문하지 않은 지점의 수를 카운트한다.
 * @returns
 */
function solution(arr) {
	let answer = 0;

	function DFS(x, y) {
		if (x <= -1 || x >= 4 || y <= -1 || y >= 5) return false;

		if (arr[x][y] === 0) {
			arr[x][y] = 1; // 방문 처리 시켜준다.

			DFS(x - 1, y); // 상
			DFS(x, y - 1);
			DFS(x + 1, y);
			DFS(x, y + 1);
			return true;
		}
		return false;
	}

	for (let i = 0; i < 4; i++) {
		for (let j = 0; j < 5; j++) {
			// 현재 위치에서 DFS 수행
			if (DFS(i, j)) {
				answer += 1;
			}
		}
	}
	return answer;
}

const arr = [
	[0, 0, 1, 1, 0],
	[0, 0, 0, 1, 1],
	[1, 1, 1, 1, 1],
	[0, 0, 0, 0, 0],
];

console.log(solution(arr));
