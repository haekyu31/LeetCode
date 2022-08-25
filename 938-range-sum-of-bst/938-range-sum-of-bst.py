# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, Node, low, high):
        if not Node:
            return 0
        Myreturn = 0
        if Node.val >=low and Node.val<=high:
            Myreturn += Node.val
        Myreturn += self.DFS(Node.left, low, high)
        Myreturn += self.DFS(Node.right, low, high)
        return Myreturn
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.DFS(root, low, high)
    