# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, root):
        if not root:
            return
        self.Answer.append(root.val)
        self.DFS(root.left)
        self.DFS(root.right)
        
            
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.Answer = []
        self.DFS(root)
        c = Counter(self.Answer)
        mx = max(c.values())
        Mx = []
        for i in c.items():
            if i[1] == mx:
                Mx.append(i[0])
        return Mx