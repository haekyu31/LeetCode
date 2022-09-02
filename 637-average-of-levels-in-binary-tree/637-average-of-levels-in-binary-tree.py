# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

            def dfs(node,depth):
                if node:
                    if len(aux) < depth:
                        aux.append([])
                    aux[depth-1].append(node.val)
                    dfs(node.left,depth+1)
                    dfs(node.right,depth+1)

            aux = []
            dfs(root,1)

            return [sum(l) / len(l) for l in aux]