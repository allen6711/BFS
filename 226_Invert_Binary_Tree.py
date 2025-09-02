# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS
        if root is None:
            return root

        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return root
    
        # DFS
        # if root is None:
        #     return root
        
        # root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        # return root