"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def DFS(self, Node):
        if not Node:
            return
        visited = []
        nextnode = []
        for nodes in Node:
            visited.append(nodes.val)
            nextnode += nodes.children
        
        self.Answer.append(visited)
        print(f'vi:{visited}, nxnd:{nextnode}, Ans:{self.Answer}')
        self.DFS(nextnode)
        
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        self.Answer = []
        self.Answer.append([root.val])
        self.DFS(root.children)
        
        
        return self.Answer