# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def DFS(self, Node, leaf):
#         if Node:
#             leaf = (leaf <<1) | Node.val
#             if not (Node.left or Node.right):
#                 self.Answer += leaf
#             self.DFS(Node.left, leaf)
#             self.DFS(Node.right, leaf)
        
#     def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
#         self.Answer = 0
#         self.DFS(root, 0)
#         return self.Answer
class Solution:
    def BinaryToDecimal(self, List):
        Level = 2**(len(List)-1)
        Sum = 0
        for value in List:
            Sum += value * Level
            Level /= 2
        return Sum
    def DFS(self, node):
        if not node:
            return
        self.Stack.append(node.val)
        # check leaf:
        if not node.left and not node.right:
            print("Leaf:", self.Stack)
            self.FinalAnswer.append(self.Stack[:])
        self.DFS(node.left)
        self.DFS(node.right)
        self.Stack.pop()
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.Stack = []
        self.FinalAnswer = []
        self.DFS(root)
        SumAllDecimal = 0
        for List in self.FinalAnswer:
            SumAllDecimal += self.BinaryToDecimal(List)
        return int(SumAllDecimal)