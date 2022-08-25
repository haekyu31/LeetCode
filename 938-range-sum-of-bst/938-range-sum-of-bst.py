# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, Node, low, high):
        if not Node:
            return
        if Node.val >=low and Node.val<=high:
            self.Answer += Node.val
            
        self.DFS(Node.left, low, high)
        self.DFS(Node.right, low, high)
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.Answer = 0
        self.DFS(root, low, high)
        return self.Answer