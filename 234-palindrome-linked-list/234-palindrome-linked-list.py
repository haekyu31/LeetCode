# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         Node = head
#         list_node = []
#         while Node : 
#             list_node.append(Node.val)
#             Node = Node.next
#         print(list_node)
        
#         #two point
#         i,j  = 0, len(list_node)-1
#         while i< j :
#             if list_node[i] != list_node[j]:
#                 return False
#             else: 
#                 i += 1
#                 j -= 1
#         return True
    
    
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        PointerNode = head
        myList = list()
        while PointerNode:
            myList.append(PointerNode.val)
            PointerNode = PointerNode.next
        return myList == list(reversed(myList))