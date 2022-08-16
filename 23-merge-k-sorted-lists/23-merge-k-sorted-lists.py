# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hq = []
        for i in lists:
            while i :
                heapq.heappush(hq, i.val)
                i = i.next
        print(hq)
        Answer = ListNode(0,None)
        Pointer = Answer
        while hq :
            Pointer.next = ListNode(heappop(hq),None)
            Pointer = Pointer.next
        return Answer.next
            
