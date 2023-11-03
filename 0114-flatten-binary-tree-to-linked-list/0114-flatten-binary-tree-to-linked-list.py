# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        stack = [root]
        temp = None
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:

                stack.append(node.left)
            if temp:
                temp.right = node
                temp.left = None
            temp = node
        

        """
        Do not return anything, modify root in-place instead.
        """
        