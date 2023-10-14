/**
최소신장트리(MST) -> greedy 알고리즘의 일종
사이클이 발생하면 안됨.
*/
function solution(n, costs) {
	var answer = 0;
	// 오름차순 정렬
	costs.sort((a, b) => a[2] - b[2]);
	let parent = [];
	for (let i = 0; i < n; i++) {
		parent.push(i); // 초기화
	}

	/* find: 재귀 이용 */
	function find(x) {
		// 부모 노드 번호로 자기 자신을 갖는다.
		if (parent[x] === x) return x;
		else return find(parent[x]); // 각 노드의 부모 노드를 찾아 올라간다.
	}

	/* union(x, y): 부모를 비교해 노드 값을 바꿔준다. */
	function union(e) {
		// 각 원소가 속한 트리의 루트 노드를 찾는다.
		console.log('e', e);
		console.log('0', find(e[0]));
		console.log('1', find(e[1]));

		let a = find(e[0]);
		let b = find(e[1]);

		if (a === b) return -1;
		else {
			if (a < b) {
				parent[b] = a;
			} else {
				parent[a] = b;
			}
		}

		return e[2];
	}

	costs.map((e) => {
		let cost = union(e);
		if (cost !== -1) {
			answer += cost;
		}
	});

	return answer;
}
