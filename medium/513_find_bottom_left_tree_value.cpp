
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
     int max_depth = -1;
     int val = 0;
     bool help_func(TreeNode* root, int depth) {
         if (root == nullptr) {
             return 0;
         }
         if (depth > max_depth) {
             max_depth = depth;
             val = root->val;
         }
         help_func(root->left, depth + 1);
         help_func(root->right, depth + 1);
         return 0;

     }
     int findBottomLeftValue(TreeNode* root) {
         help_func(root, 0);
         return val;
     }
 };

void main() {
    Solution s = Solution();
}