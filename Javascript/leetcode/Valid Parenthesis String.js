/**
 * @param {string} s
 * @return {boolean}
 */
var checkValidString = function (s) {
	/**
  map 안에 (, *, ) 갯수를 넣는다. 
  만약 *이 오면 (나 )로 치환해주는데, 두 값을 뻇을 경우 *의 갯수와 같으면 true, 아니면 false
   */
	const map = new Map();
	for (let i = 0; i < s.length; i++) {
		map.set(s[i], (map.get(s[i]) || 0) + 1);
	}
	console.log(map);

	if (Number(map.get('(')) === Number(map.get(')'))) return true;
	else {
		console.log('* 갯수', Number(map.get('*')));
		console.log(
			'abs 갯수',
			Math.abs(Number(map.get('(')) - Number(map.get(')')))
		);
		if (
			Number(map.get('*')) >=
			Math.abs(Number(map.get('(')) - Number(map.get(')')))
		)
			return true;
		return false;
	}
};

s =
	'(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())';
console.log(checkValidString(s));

// ----------------- 위에가 Map 이용해서 처음 이용했던 방식, 아래가 Stack 사용해서 순서대로 이용한 방식

/**
 * @param {string} s
 * @return {boolean}
 */
var checkValidString = function (s) {
	/**
  map 안에 (, *, ) 갯수를 넣는다. 
  만약 *이 오면 (나 )로 치환해주는데, 두 값을 뻇을 경우 *의 갯수보다 작으면 true. 
  왜냐하면 *가 빈 스트링이 되면 되니까.
  -> 이렇게 하면 순서 보장이 안됨..
   */
	let leftStack = [];
	let starStack = [];
	for (let i = 0; i < s.length; i++) {
		switch (s[i]) {
			case '(':
				leftStack.push(i);
				break;
			case ')':
				if (leftStack.length > 0) {
					leftStack.pop();
				} else if (starStack.length > 0) {
					starStack.pop();
				} else {
					return false;
				}
				break;
			case '*':
				starStack.push(i);
				break;
		}
	}
	while (leftStack.length > 0 && starStack.length > 0) {
		if (leftStack[leftStack.length - 1] > starStack[starStack.length - 1]) {
			return false;
		}
		leftStack.pop();
		starStack.pop();
	}
	if (leftStack.length > 0) return false;
	return true;
};
