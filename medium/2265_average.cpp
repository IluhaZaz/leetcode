  struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
  };

#include <utility>
using namespace std;

class Solution {
public:

    pair<int, int> count(TreeNode* root, int& c){
        if(!root){
            return pair<int, int>(0, 0);
        }
        pair<int, int> l = count(root->left, c);
        pair<int, int> r = count(root->right, c);

        int s = l.first + r.first + root->val;
        int k = l.second + r.second + 1;
        if(s/k == root->val)
            c++;
        return pair<int, int>(s, k);
    }

    int averageOfSubtree(TreeNode* root) {
        int c = 0;
        count(root, c);
        return c;
    }
};