# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root : return []
        Answer = []
        self.inorder(root, Answer)
        return Answer
   
    def inorder(self, root, Answer):
        if root:
            self.inorder(root.left, Answer)
            self.inorder(root.right, Answer)
            Answer.append(root.val)