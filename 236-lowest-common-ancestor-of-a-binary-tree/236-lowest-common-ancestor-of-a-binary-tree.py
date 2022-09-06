# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def DFS(self, node):
        if not node:
            return 0    
        Descent = self.DFS(node.left) + self.DFS(node.right)
        if node.val == self.p:
            Descent = Descent + 1
        if node.val == self.q:
            Descent = Descent + 1
        if Descent == 2:
            if self.Answer == 0:
                self.Answer = node
        return Descent
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.Answer = 0
        self.p = p.val
        self.q = q.val
        self.DFS(root)
        return self.Answer