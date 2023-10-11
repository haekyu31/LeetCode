# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        rightPointer = head
        leftPointer = head
        counter = 0
        while rightPointer != None:
            counter += 1
            if counter != k and counter<k:
                leftPointer = leftPointer.next
            rightPointer = rightPointer.next
        rightPointer = head
        for i in range(counter-k):
            rightPointer = rightPointer.next
        temp = leftPointer.val
        leftPointer.val = rightPointer.val
        rightPointer.val = temp
        return head
        