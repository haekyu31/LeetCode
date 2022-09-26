# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = 0
        node = head
        while head:
            pointer +=1
            head = head.next
        cnt = 0
        while node:
            if cnt == pointer//2:
                break
            cnt +=1
            node = node.next
        return node
            
            