# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        if not head:
            return head
        
        Node = head
        while Node and Node.next:
            if Node.next.val == val:
                Node.next = Node.next.next
            else:
                Node = Node.next
                
        return head