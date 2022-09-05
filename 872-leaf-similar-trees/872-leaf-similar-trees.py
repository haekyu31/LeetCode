# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, root, li):
        if not root:
            return 
        self.DFS(root.left, li)
        if not(root.left or root.right):
            li.append(root.val)
        self.DFS(root.right, li)
        print(li)
        return li
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return (self.DFS(root1, [])== self.DFS(root2, []))