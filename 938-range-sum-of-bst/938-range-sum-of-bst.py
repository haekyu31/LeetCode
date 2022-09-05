# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = [root]
        node_sum = 0
        if not root:
            return
        while queue:            # 모든 queue를 돌면 종료하도록 while을 사용한다.
            value = queue.pop(0)  # 1개의 값을 먼저 계산하기 위해서 pop으로 꺼내온다.
            if low<= value.val <=high:  #조건을 만족하면 저장한다.
                node_sum += value.val
            if value.left:              #다음 연결된 root가 있다면 이동할수 있도록 visited queue에 집어 넣는다.
                queue.append(value.left)
            if value.right:             #같은 높이의 root를 집어넣는다.
                queue.append(value.right)
        return node_sum
