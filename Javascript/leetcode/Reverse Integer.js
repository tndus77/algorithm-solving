/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
	const MAX_INT = 2 ** 31 - 1;
	const MIN_INT = -(2 ** 31);
	const temp = [];
	const s = x.toString().split('');
	for (let i = 0; i < s.length; i++) {
		temp.push(s[i]);
	}
	let result = 0;
	if (temp.includes('-')) {
		result = temp.shift() + temp.reverse().join('');
		if (result < MIN_INT) return 0;
		return result;
	} else {
		result = temp.reverse().join('');
		if (result <= MAX_INT) return result;
		return 0;
	}
};
