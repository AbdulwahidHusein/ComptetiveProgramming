from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        que = deque()
        max_rows = []
        que.append(root)

        while que:
            curr_leng = len(que)
            max_now = -float('inf')

            for _ in range(curr_leng):
                node = que.popleft()
                max_now = max(max_now, node.val)
            
                for nd in [node.left, node.right]:
                    if nd:
                        que.append(nd)
            max_rows.append(max_now)
        return max_rows







        