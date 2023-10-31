from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, path, path_sum):
            if node is None:
                return

            path.append(node.val)
            path_sum += node.val

            if node.left is None and node.right is None:
                if path_sum == targetSum:
                    result.append(path.copy())

            dfs(node.left, path, path_sum)
            dfs(node.right, path, path_sum)

            path.pop()
            path_sum -= node.val

        dfs(root, [], 0)
        return result
