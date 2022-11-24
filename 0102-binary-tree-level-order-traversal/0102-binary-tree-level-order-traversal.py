# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(k):
            if len(k) == 0:
                return
            ans, newk = [], []
            for node in k:
                ans.append(node.val)
                
                if node.left:
                    newk.append(node.left)
                if node.right:
                    newk.append(node.right)
            res.append(ans)
            dfs(newk)
            return
        res = []
        if root:
            dfs([root])
        return res
#         if not root:
#             return []
        
#         def findDepth(cur=root, depth=0):
#             if not cur:
#                 return depth
#             return max(findDepth(cur.left, depth + 1), findDepth(cur.right, depth + 1))
        
#         output, stack = [[] for _ in range(findDepth())], [(root, 0)]
#         while stack:
#             cur, depth = stack.pop()
#             if cur.right:
#                 stack.append((cur.right, depth+1))
#             if cur.left:
#                 stack.append((cur.left, depth +1))
#             output[depth].append(cur.val)
#         return output