# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        val = 0
        if root is None:
            return val
        val = max(self.maxDepth(root.left)+1, 1+self.maxDepth(root.right))
        return val

