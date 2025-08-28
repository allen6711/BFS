# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS
        if not p and not q:
            return True

        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # BFS
        # queue = deque([(p, q)])
        
        # while queue:
        #     root_p, root_q = queue.popleft()
            
        #     if not root_p and not root_q:
        #         continue
                
        #     if not root_p or not root_q:
        #         return False
            
        #     if root_p.val != root_q.val:
        #         return False
            
        #     queue.append((root_p.left, root_q.left))
        #     queue.append((root_p.right, root_q.right))
        
        # return True
    
if __name__ == "__main__":
    sol = Solution()
    result = sol.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3)))
    print(result)