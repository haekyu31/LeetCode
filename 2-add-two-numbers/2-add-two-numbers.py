# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = Pointer = ListNode(0)
        plus = 0
        while l1 or l2 or plus : 
            if l1 :
                plus += l1.val
                l1 = l1.next
            if l2 :
                plus += l2.val
                l2 = l2.next
            Pointer.next = ListNode(plus%10)
            Pointer = Pointer.next
            plus //= 10
        return head.next