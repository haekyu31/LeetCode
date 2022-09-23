# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head 
        fast = head
 
        while fast and fast.next :
            #slow jumps one step further
            #fast jumps two steps forward
            slow = slow.next
            fast = fast.next.next
             #At some point fast meets slow if loop is found in linked list 
            if  fast == slow:
                return True
        return False
               