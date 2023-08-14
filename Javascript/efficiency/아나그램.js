function solution(arr1, arr2) {
	let answer = 'YES';
	let sH1 = new Map();
	for (let x of arr1) {
		if (sH1.has(x)) {
			sH1.set(x, sH1.get(x) + 1);
		} else {
			sH1.set(x, 1);
		}
	}
	for (let x of arr2) {
		if (sH1.has(x)) {
			sH1.set(x, sH1.get(x) - 1);
		}
		if (sH1.get(x) < 0) {
			answer = 'NO';
			return answer;
		}
	}
	return answer;
}

const arr1 = 'abaCC';
const arr2 = 'Caaab';
console.log(solution(arr1, arr2));
