# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def Recur(self, Node, target):
        if Node.val == target.val:
            return Node
        
        if Node.left:
            RetNode = self.Recur(Node.left, target)
            if type(RetNode) == TreeNode:
                return RetNode
        if Node.right:
            RetNode = self.Recur(Node.right, target)
            if type(RetNode) == TreeNode:
                return RetNode
                
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        Answer = self.Recur(cloned, target)
        return Answer