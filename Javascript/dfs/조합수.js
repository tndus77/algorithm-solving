/**
 * 조합 (메모이제이션 이용)
 * -> 큰 수는 시간 제한 걸림.
 */
function solution(n, r) {
	let answer;
	// memoization 이용
	const dy = Array.from({ length: 11 }, () => Array(11).fill(0)); // 11 x 11 배열 생성
	function DFS(n, r) {
		if (dy[n][r] > 0)
			// 이미 이전에 호출된 것
			return dy[n][r];
		if (n === r || r === 0) return 1;
		else return (dy[n][r] = DFS(n - 1, r - 1) + DFS(n - 1, r));
	}
	answer = DFS(n, r);
	return answer;
}

console.log(solution(45, 19));
