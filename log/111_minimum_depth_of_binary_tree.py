#Date: 033022
#Difficulty: Easy
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        minDepth=float('inf')
        stack=[(root,1)]
        while stack:
            node,depth=stack.pop()
            if node.left:
                stack.append((node.left,depth+1))
            if node.right:
                stack.append((node.right,depth+1))
            if not node.left and not node.right:
                minDepth=min(minDepth,depth)
        return minDepth
