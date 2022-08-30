# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def invertTree(self, root):
    #     if root:
    #         root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    #         return root
        
#     def invertTree(self, root):
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             if node:
#                 node.left, node.right = node.right, node.left
#                 stack += node.left, node.right
#         return root
    
#     def invertTree2(self, root):
#         queue = collections.deque([(root)])
#         while queue:
#             node = queue.popleft()
#             if node:
#                 node.left, node.right = node.right, node.left
#                 queue.append(node.left)
#                 queue.append(node.right)
#         return root
    
    def invertTree(self, root):
        if root :
            root.left, root.right = root.right, root.left
            if root.left:
                self.invertTree(root.left)
            if root.right:
                self.invertTree(root.right)
            return root
        else:
            return 

    