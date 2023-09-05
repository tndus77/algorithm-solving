/**
 * @param {number[]} nums
 * @return {boolean}
 */
/**
 * 현재 반복문 지점 i와 max를 비교해서 i가 더 크면 false를 반환한다.
 * 왜냐하면 i번째 인덱스까지 도달할 수 없다는 뜻이기 때문.
 *
 * 아니라면 현재 i번째 인덱스 값과 i를 더해 max에 저장한다.
 * 즉, max 값은 최대 어느 인덱스까지 점프할 수 있는지 저장하는 것이다.
 */
var canJump = function (nums) {
	let max = 0;
	for (let i = 0; i < nums.length; i++) {
		if (i > max) return false;
		max = Math.max(nums[i] + i, max);
	}
	return true;
};
