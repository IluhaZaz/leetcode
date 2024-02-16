  struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
  };
 
class Solution {
public:

    int help(TreeNode* root, bool left) {
        if (!root) {
            return 0;
        }
        if (!root->left && !root->right)
            return root->val * left;
        return help(root->left, 1) + help(root->right, 0);
    }

    int sumOfLeftLeaves(TreeNode* root) {
        if (!root) {
            return 0;
        }
        return help(root, 0);
    }
};