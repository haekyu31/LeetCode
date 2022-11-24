# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        res = []
        def dfs(node, parent, depth):
            if not node:
                return
            if node.val == x or node.val == y:
                res.append((parent, depth))
            dfs(node.left, node, depth+1)
            dfs(node.right, node, depth+1)
            
        dfs(root, None, 0)
        
        node_x, node_y = res
        
        return node_x[0] != node_y[0] and node_x[1] == node_y[1]
#         res = []
        
#         queue = deque([(root, None, 0)])
#         while queue:
#             if len(res) == 2:
#                 break
#             node, parent, depth = queue.popleft()
#             if node.val ==x or node.val ==y:
#                 res.append((parent, depth))
#             if node.left:
#                 queue.append((node.left, node, depth+1))
#             if node.right:
#                 queue.append((node.right, node, depth+1))
#         node_x, node_y = res
        
#         return node_x[0] != node_y[0] and node_x[1] == node_y[1]