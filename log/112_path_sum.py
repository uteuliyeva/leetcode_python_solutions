#Date: 040322
#Difficulty: Easy
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        stack=[(root,targetSum)]
        while stack:
            node,target=stack.pop()
            if not node.left and not node.right and node.val==target:
                return True
            if node.left:
                stack.append((node.left,target-node.val))
            if node.right:
                stack.append((node.right,target-node.val))
        return False
