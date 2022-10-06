# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    head = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        def rev_preorder(node):
            if node.right: 
                rev_preorder(node.right)
            if node.left: 
                rev_preorder(node.left)
            node.left, node.right, self.head = None, self.head, node
        if root: rev_preorder(root)