# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        visited = []
        node_sum = 0
        visited.append(root)
        while True:
            n = len(visited)
            if n<= 0 :
                break
            if n>0:
                node = visited.pop(0)
                if low <=node.val<=high:
                    node_sum +=node.val
                if node.left:
                    visited.append(node.left)
                if node.right:
                    visited.append(node.right)
                n -= 1
        return node_sum