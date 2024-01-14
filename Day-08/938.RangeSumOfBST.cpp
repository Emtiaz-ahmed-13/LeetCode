

// problem Link:
//     https://leetcode.com/problems/range-sum-of-bst/


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        if(!root) return 0;
        int ans=0;
        int val=root->val;
        if(val>=low && val <=high)
        {
            ans+=val+rangeSumBST(root->left,low,high)+rangeSumBST(root->right,low,high);
        }
        else if(val<low)
        {
            ans+=rangeSumBST(root->right,low,high);
        }
        else if(val>high)
        {
            ans+=rangeSumBST(root->left,low,high);
        }
            return ans;

        
    }
};