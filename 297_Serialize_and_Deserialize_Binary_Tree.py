# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '{}'
        
        queue = [root]
        index = 0
        
        while index < len(queue):
            if queue[index] is not None:
                queue.append(queue[index].left)
                queue.append(queue[index].right)
            index += 1
        
        while queue[-1] is None:
            queue.pop()
        
        return '{%s}' % ','.join([str(node.val) if node is not None else '#' for node in queue])
            


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.strip('\n')
        
        if data == '{}':
            return None
        
        # 頭尾是{}
        vals = data[1:-1].split(',')
        root = TreeNode(int(vals[0]))
        queue = [root]
        index = 0
        isLeftChild = True
        
        for val in vals[1:]:
            if val is not '#':
                node = TreeNode(int(val))
                if isLeftChild:
                    queue[index].left = node
                else:
                    queue[index].right = node
                
                queue.append(node)
            
            if not isLeftChild:
                index += 1
            
            isLeftChild = not isLeftChild
        
        return root        
        
if __name__ == "__main__":
    ser = Codec()
    result = ser.serialize(TreeNode(1, TreeNode(2, None, None), TreeNode(3, TreeNode(4), TreeNode(5))))
    print(result)

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))