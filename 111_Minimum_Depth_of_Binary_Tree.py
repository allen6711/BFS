# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # BFS
        if root is None:
            return 0
        
        # root and depth
        queue = deque([(root, 1)])
        
        while queue:
            node, depth = queue.popleft()
            if node.left is None and node.right is None:
                return depth
            
            if node.left:
                queue.append((node.left, depth + 1))
            
            if node.right:
                queue.append((node.right, depth + 1))
        
        return depth
    
        # DFS
        # if root is None:
        #     return 0

        # if root.left is None and root.right is not None:
        #     return 1 + self.minDepth(root.right)
        
        # if root.right is None and root.left is not None:
        #     return 1 + self.minDepth(root.left)
        
        # return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

if __name__ == '__main__':
    sol = Solution()
    result = sol.minDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
    print(result)
    result = sol.minDepth(TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6))))))
    print(result)