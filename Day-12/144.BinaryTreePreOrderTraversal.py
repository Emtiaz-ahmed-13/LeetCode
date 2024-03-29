
# Problem Link:
#     https://leetcode.com/problems/binary-tree-preorder-traversal/description/

from ast import List
from typing import Optional


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        if root:
            res+= [root.val]
            res+= self.preorderTraversal(root.left)
            res+= self.preorderTraversal(root.right)
        return res

