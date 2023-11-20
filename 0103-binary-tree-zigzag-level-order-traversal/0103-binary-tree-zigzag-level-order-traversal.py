# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque()
        queue.append(root)
        odd = 0
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            if level:
                if odd % 2 == 0:
                    result.append(level)
                else:
                    result.append(level[::-1])
            odd += 1
        return result