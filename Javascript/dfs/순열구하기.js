function solution(n, m, testArr) {
	const arr = testArr.split(' ').map((i) => +i);
	const check = Array.from({ length: n }, () => 0);
	const temp = Array.from({ length: m }, () => 0);
	let answer = [];

	function DFS(L) {
		if (L === m) {
			answer.push(temp.slice());
		} else {
			for (let i = 0; i < n; i++) {
				if (check[i] === 0) {
					check[i] = 1;
					temp[L] = arr[i];
					DFS(L + 1);
					// back
					check[i] = 0;
				}
			}
		}
	}
	DFS(0);
	return answer;
}

const [n, m] = [3, 2];
const testArr = '3 6 9';
console.log(solution(n, m, testArr));
