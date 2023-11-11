# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        targs = {}
        def dfs(root, target):
            if not root:
                return False
            if root.val in targs:
                return True
            targs[target-root.val] = 0
            return dfs(root.left, target) or dfs(root.right, target)
        return dfs(root, k)
            
            
