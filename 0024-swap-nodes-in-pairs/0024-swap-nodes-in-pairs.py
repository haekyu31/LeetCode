# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head and head.next:  # pair가 존재할 경우
#             p = head.next       # pointer에 head.next를 담아두고 
#             #스왑된 값 리턴 받음
#             head.next = self.swapPairs(p.next)  # head.next에는 p.next 즉 head.next.next를 연결해준다. 
#             p.next = head       # head.next를 담고 있는 p는 p.next로 head를 연결하여 pair단위로 스왑이 되도록한다.
#             return p
#         return head             # head나 head.next가 존재하지 않을 경우 남은 head나 None를 return한다. 
        root = prev = ListNode(None)
        prev.next = head            # None을 갖는 prev를 지정하여 head와 연결해준다.
        
        while head and head.next:   # pair가 존재하는 경우
            # b가 a(head)를 가리키도록 할당
            b = head.next           # b에 head.next를 담아두고
            head.next = b.next      # head와 연결된것은 head.next.next인 b.next를 연결해준다 pair를 이루기위해
            b.next = head           # b는 head와 연결하여 역방향을 완성시킨다.
            
            # prev가 b를 가리키도록 할당
            prev.next = b           # None이었던 prev와 b를 연결해준다.
            
            # 다음번 비교를 위해 이동
            head = head.next
            prev = prev.next.next
        return root.next
            
    
    