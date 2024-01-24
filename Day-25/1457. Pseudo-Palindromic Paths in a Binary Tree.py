# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def updatePath(value: int) -> None:

            if value in path:
            
                path.remove(value)
            
            else:
    
                path.add(value)
        
        def dfs(node: Optional[TreeNode]) -> int:
     
            if node is None:
               
                return 0
            value = node.val
            left = node.left
            right = node.right
            result = 0
            
         
            updatePath(value)

           
            if (left, right) == (None, None):
                
                 result = int(len(path) < 2)
   
            else:
                result = dfs(left) + dfs(right)

            updatePath(value)
            
   
            return result
        path = set()
    
        return dfs(root)
        