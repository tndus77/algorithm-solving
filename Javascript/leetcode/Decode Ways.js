/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function (s) {
	let n = s.length;
	let dp = new Array(n + 1).fill();
	dp[0] = 1; // 빈 문자열은 하나의 해독방법만 있음.
	dp[1] = s[0] === '0' ? 0 : 1; // 첫 번째 숫자가 0이면 해독할 수 없음.

	for (let i = 2; i <= s.length; i++) {
		let oneDigit = parseInt(s[i - 1]);
		let twoDigit = parseInt(s.substring(i - 2, i));

		// 한 자리 숫자를 해독할 수 있다면, 1칸 이전의 해독 방법의 수를 더한다.
		if (oneDigit >= 1) {
			dp[i] += dp[i - 1];
		}

		// 두 자리 숫자를 해독할 수 있다면, 2칸 이전의 해독 방법의 수를 더한다.
		if (twoDigit >= 10 && twoDigit <= 26) {
			dp[i] += dp[i - 2];
		}
	}
	return dp[n];
};
