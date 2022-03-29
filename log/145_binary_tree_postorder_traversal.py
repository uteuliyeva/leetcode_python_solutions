#Date: 032922
#Difficulty: Easy
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output=[]
        if root:
            output=self.postorderTraversal(root.left)
            output+=self.postorderTraversal(root.right)
            output.append(root.val)
        return output
