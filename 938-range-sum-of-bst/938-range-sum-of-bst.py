# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = [root]
        node_sum = 0
        if not root:
            return
        while queue:
            value = queue.pop(0)
            if low<= value.val <=high:
                node_sum += value.val
            if value.left:
                queue.append(value.left)
            if value.right:
                queue.append(value.right)
        return node_sum
