# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        # Since we know input node is not last node, so nextNode will not be null
        nextNode = node.next
        # Step 2
        node.val = nextNode.val
        # Step 3
        node.next = nextNode.next
        nextNode.next = None
        del(nextNode)