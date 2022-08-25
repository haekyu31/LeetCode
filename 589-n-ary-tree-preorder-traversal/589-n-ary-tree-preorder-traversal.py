"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def DFS(self, Node):
        self.Answer.append(Node.val)
        if Node.children :
            for child in Node.children:
                self.DFS(child)
    
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        self.Answer = []
        self.DFS(root)
        return self.Answer
            
            