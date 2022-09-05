# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
    # def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    #     # print(f'root: {root}')
    #     queue = [root]
    #     node_sum = 0
    #     if not root:
    #         return 
    #     while queue:
    #         # print([Idx.val for Idx in queue])
    #         value = queue.pop(0)
    #         if value.left:
    #             queue.append(value.left)
    #             if not (value.left.left or value.left.right):
    #                 node_sum += value.left.val
    #         if value.right:
    #             queue.append(value.right)
    #     return node_sum
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q, ans = deque([(root, False)]), 0
        while q:
            cur, isLeft = q.popleft()
            if not cur.left and not cur.right and isLeft:
                ans = ans + cur.val
            if cur.right:
                q.append((cur.right, False))
            if cur.left: 
                q.append((cur.left, True))
        return ans