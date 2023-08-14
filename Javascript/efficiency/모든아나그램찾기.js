function solution(arr1, arr2) {
	let sH1 = new Map();
	let count = 0;
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
			count += 1;
		}
	}
	return count;
}

const arr1 = 'bacaAacba';
const arr2 = 'abc';
console.log(solution(arr1, arr2));

/**
 * 수정 필요
 */
