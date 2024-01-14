
# problem Link:
#     https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/
    
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
    
        from collections import defaultdict, deque

        adj = defaultdict(list)
        def buildTree(root):
            if root is None:
                return
            if root.left:
                adj[root.val].append(root.left.val)
                adj[root.left.val].append(root.val)
                buildTree(root.left)
            if root.right:
                adj[root.val].append(root.right.val)
                adj[root.right.val].append(root.val)
                buildTree(root.right)
        
        buildTree(root)
                
        q = deque()
        q.append(start)
        visited = set()
        visited.add(start)
        count = 0
        while q:
            size = len(q)
            while size:
                e = q.popleft() 	
                visited.add(e)
                for n in adj[e]:
                    if n not in visited:
                        q.append(n)
                size -= 1	
            count+=1

        return count-1