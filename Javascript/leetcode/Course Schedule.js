/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function (numCourses, prerequisites) {
	const graph = new Map();
	const temp = []; // 사이클이 발생하면 안되므로, 원소 중복 검사
	const visited = []; // 해당 그래프를 탐색했는지, 했으면 통과

	for (const [v, e] of prerequisites) {
		graph.set(v, [...(graph.get(v) || []), e]);
	}

	const DFS = (v) => {
		const edges = graph.get(v);
		if (!edges) return false;
		else {
			for (const edge of edges) {
				if (visited.includes(edge)) continue;
				else {
					if (v === edge || temp.includes(edge)) return true;
					temp.push(edge);
					if (DFS(edge)) return true;
					temp.pop(edge);
					visited.push(edge);
				}
			}
		}
	};

	for (const [v, e] of graph) {
		if (DFS(v)) return false;
	}
	return true;
};
