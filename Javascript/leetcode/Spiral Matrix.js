/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
	if (!matrix || matrix.length === 0) {
		return [];
	}

	const result = [];
	let top = 0;
	let right = matrix[0].length - 1;
	let bottom = matrix.length - 1;
	let left = 0;

	while (top <= bottom && left <= right) {
		// 위쪽 가로줄
		for (let i = left; i <= right; i++) {
			result.push(matrix[top][i]);
		}
		top++;

		// 오른쪽 세로줄
		for (let i = top; i <= bottom; i++) {
			result.push(matrix[i][right]);
		}
		right--;

		// 아래 가로줄
		if (top <= bottom) {
			// top이 bottom을 넘으면 이미 위쪽 가로줄을 방문한 상태이므로 더 이상 아래로 이동할 필요 X
			for (let i = right; i >= left; i--) {
				result.push(matrix[bottom][i]);
			}
			bottom--;
		}

		// 왼쪽 세로줄
		if (left <= right) {
			// left가 right을 넘을 경우 이미 오른쪽 세로줄을 방문한 상태이므로 더 이상 왼쪽으로 이동할 필요 X
			for (let i = bottom; i >= top; i--) {
				result.push(matrix[i][left]);
			}
			left++;
		}
	}
	return result;
};
