/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function (root) {
	return validate(root, -Infinity, Infinity);
};

function validate(node, min, max) {
	if (!node) return true; // 빈 노드는 유효하다고 간주

	if (min < node.val && node.val < max)
		return (
			validate(node.left, min, node.val) && validate(node.right, node.val, max)
		);
	else return false;
}
