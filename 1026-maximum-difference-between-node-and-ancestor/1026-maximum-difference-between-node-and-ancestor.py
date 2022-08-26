# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, Node, low = 10**5+1, high = -1):
        if not Node:
            self.Answer.append(abs(high - low))
            return 
        if Node.val < low:
            low = Node.val
        if Node.val > high:
            high = Node.val
        
        self.DFS(Node.left, low, high)
        self.DFS(Node.right, low, high)
        return #max(self.Answer)
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.Max, self.Min = -1, 10**5+1
        self.Answer =[]
        self.DFS(root)
        return max(self.Answer)