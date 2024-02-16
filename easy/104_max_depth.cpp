class Solution {
public:

	int help_get_height(TreeNode* root, int lvl) {
		if (root == nullptr) {
			return lvl - 1;
		}
		return max(help_get_height(root->left, lvl + 1), help_get_height(root->right, lvl + 1));

	}

	int maxDepth(TreeNode* root) {
		return help_get_height(root, 1);
	}
};