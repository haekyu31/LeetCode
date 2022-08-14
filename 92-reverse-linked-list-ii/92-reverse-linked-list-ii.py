# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        Pointer = ListNode(0)
        Pointer.next = head
        dummy = Pointer
        for i in range(left-1):
            dummy = dummy.next
            
        P0 = None
        P1 = dummy.next
        for i in range(right - left +1):
            P2 = P1.next
            P1.next = P0
            P0 = P1
            P1 = P2
        dummy.next.next = P1
        dummy.next= P0
        
        return Pointer.next