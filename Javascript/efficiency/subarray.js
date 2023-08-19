function solution(nums) {
	nums.forEach((val, idx) => {
		if (nums[idx - 1] > 0) {
			nums[idx] += nums[idx - 1];
		}
	});

	return Math.max(...nums);
}

const nums = [-2, 0, -1];
console.log(solution(nums));
