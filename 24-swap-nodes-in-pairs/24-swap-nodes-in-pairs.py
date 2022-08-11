# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Pointer = ListNode(0)  # dummy linked list
        Pointer.next = ListNode(0)
        Answer = Pointer
        
        while head :
            if head.next != None : 
                first = head
                second = head.next
                new_head = second.next 
                second.next = first
                first.next = None
                Pointer.next.next = second
                Pointer = Pointer.next.next
                head = new_head
            else :
                Pointer.next.next = head
                break
        return Answer.next.next
            
        
