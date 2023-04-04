# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:                        # node가 끝나면
                return prev                     # 역순으로 저장된 prev를 return한다.
            next, node.next = node.next, prev   # next에 node.next를 설정해두고 node.next에는 prev를 저장해둔다.
            return reverse(next, node)          # node.next에 대해서 역방향인 node로 recursive를 확인
                                                # prev는 뒤집힌 연결 리스트의 첫 번째 노드가 된다.
        return reverse(head)
#         node, prev = head, None               # node에 head를 prev에 None를 저장
        
#         while node:                           # linked list를 따라가면서
#             next, node.next = node.next, prev # next에 node.next자료를 저장하고 node.next에는 이전 list인 prev를 연결해준다
#             prev, node = node, next           # prev에 node를 넣고, node는 next의 자료를 가져와서 역방향으로 돌게한다.
#         return prev                           # 역방향 첫번째 노드인 prev를 return한다.