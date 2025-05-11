# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        current_node = head

        while current_node:

            while current_node.next and current_node.val == current_node.next.val:

                current_node.next = current_node.next.next

            current_node = current_node.next

        return head
        