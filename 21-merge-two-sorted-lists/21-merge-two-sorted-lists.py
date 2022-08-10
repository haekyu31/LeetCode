# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
#         root = Answer = ListNode()
#         print(Answer)
#         while list1 or list2 :
#             if list1 and list2:
#                 if list1.val < list2.val : 
#                     value = list1.val
#                     list1 = list1.next
#                 else : 
#                     value = list2.val
#                     list2 = list2.next
#             elif list1:
#                 value = list1.val
#                 list1 = list1.next
#             elif list2:
#                 value = list2.val
#                 list2 = list2.next
#             print(value)
#             Answer.next = ListNode(value)
#             Answer = Answer.next
            
#         return root.next
        
#     #새로운 Linked List에 추가한다
#         Header = ListNode(0)
#         Pointer = Header
        
#         while list1 and list2:
#             if list1.val< list2.val:
#                 Pointer.next = ListNode(list1.val)
#                 Pointer = Pointer.next
#                 list1 = list1.next
#             else: 
#                 Pointer.next = ListNode(list2.val)
#                 Pointer = Pointer.next
#                 list2 = list2.next
        
#         while list1:
#             Pointer.next = ListNode(list1.val)
#             Pointer = Pointer.next
#             list1 = list1.next
#         while list2:
#             Pointer.next = ListNode(list2.val)
#             Pointer = Pointer.next
#             list2 = list2.next
            
#         return Header.next

        Header = Pointer =ListNode(0)
        
        while list1 and list2:
            if list1.val < list2.val:
                Pointer.next = list1
                Pointer = Pointer.next
                list1 = list1.next
            else:
                Pointer.next = list2
                Pointer = Pointer.next
                list2 = list2.next
        if list1:
            Pointer.next = list1
        
        if list2:
            Pointer.next = list2
            
        return Header.next
    
    # class Solution:
    # def mergeTwoLists(self, list1, list2) -> Optional[ListNode]:
    #     Header = Pointer = ListNode(0, None)
    #     while list1 and list2:
    #         if list1.val < list2.val:
    #             Pointer.next = list1
    #             Pointer = Pointer.next
    #             list1 = list1.next
    #         else:
    #             Pointer.next = list2
    #             Pointer = Pointer.next
    #             list2 = list2.next
    #     if list1:
    #         Pointer.next = list1
    #     if list2:
    #         Pointer.next = list2
    #     return Header.next

                