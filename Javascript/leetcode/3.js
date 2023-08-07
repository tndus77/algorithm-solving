/**
 * 문제 https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
	let substr = ''; // 겹치치 않는 문자열 저장
	let count = 0;
	for (let i = 0; i < s.length; i++) {
		if (substr.includes(s[i])) {
			// 만약 substr에 포함되어 있으면
			// 포함되어 있는 s[i]의 인덱스를 찾아서 +1부터 끝까지 배열을 자른다.
			substr = substr.slice(substr.indexOf(s[i]) + 1);
		}
		substr += s[i];
		if (count < substr.length) {
			count = substr.length;
		}
	}
	return count;
};
