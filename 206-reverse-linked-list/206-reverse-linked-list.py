# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #two poin prev
        
        Prev = None
        Pointer = head
        while Pointer:
            Next = Pointer.next
            Pointer.next = Prev
            
            Prev = Pointer
            Pointer = Next
            
        return Prev