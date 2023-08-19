function increasingTriplet(nums) {
	const dp = Array.from({ length: nums.length }, () => 0);
	dp[0] = 1;
	for (let i = 0; i < nums.length; i++) {
		let max = 0;
		for (let j = i - 1; j >= 0; i--) {
			if (nums[j] <= nums[i] && dp[j] > max) {
				max = dp[j];
			}
		}
		dp[i] = max + 1;
	}
	if (dp.length >= 3) return true;
	else return false;
}

const nums = [1, 2, 3, 4, 5];
console.log(increasingTriplet(nums));
