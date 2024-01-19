# Problem  Link: 
#         https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

from typing import Optional


class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, root.val, root.val)

    def helper(self, r, mn, mx):
        if not r:
            return mx - mn
        mn = min(mn, r.val)
        mx = max(mx, r.val)

        left_diff = self.helper(r.left, mn, mx)
        right_diff = self.helper(r.right, mn, mx)

        return max(left_diff, right_diff)
    
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def helper(node, current_min, current_max):
            if not node:
                return current_max - current_min
            
            current_min = min(node.val, current_min)
            current_max = max(node.val, current_max)

            left_diff = helper(node.left, current_min, current_max)
            right_diff = helper(node.right, current_min, current_max)
            
            return max(left_diff, right_diff)
        
        return helper(root, root.val, root.val)
