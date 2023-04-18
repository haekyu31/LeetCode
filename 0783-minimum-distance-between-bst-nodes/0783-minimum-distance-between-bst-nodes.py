# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = -sys.maxsize
    result = sys.maxsize
    
    # 재귀 구조 중위 순회 비교 결과
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # BST의 특성 바로 오른쪽 자식과 비교하거나 왼쪽 자식의 가장 오른쪽 자식과 비교하기
        if root.left:
            self.minDiffInBST(root.left)
            
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)
        
        return self.result
        