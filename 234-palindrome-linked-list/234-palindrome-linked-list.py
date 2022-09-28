# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        Node = head
        while Node:
            nums.append(Node.val)
            Node = Node.next
        print(nums)
        i, j  = 0, len(nums)-1
        while i<j:
            if nums[i] !=nums[j]:
                return False
            else:
                i +=1
                j -=1
        return True