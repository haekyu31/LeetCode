# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = Answer = ListNode()
        print(Answer)
        while list1 or list2 :
            if list1 and list2:
                if list1.val < list2.val : 
                    value = list1.val
                    list1 = list1.next
                else : 
                    value = list2.val
                    list2 = list2.next
            elif list1:
                value = list1.val
                list1 = list1.next
            elif list2:
                value = list2.val
                list2 = list2.next
            print(value)
            Answer.next = ListNode(value)
            Answer = Answer.next
            
        return root.next
        