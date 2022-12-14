"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        return 1 + max(map(self.maxDepth, root.children or [None]))