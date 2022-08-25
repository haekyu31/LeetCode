# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, Node, leaf):
        if Node:
            leaf = (leaf <<1) | Node.val
            if not (Node.left or Node.right):
                self.Answer += leaf
            self.DFS(Node.left, leaf)
            self.DFS(Node.right, leaf)
        
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.Answer = 0
        self.DFS(root, 0)
        return self.Answer