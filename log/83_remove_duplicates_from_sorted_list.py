#Date: 031722
#Difficulty: Easy
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        slow=head
        fast=head.next
        while fast:
            if slow.val!=fast.val:
                slow.next=fast
                slow=slow.next
            fast=fast.next
        slow.next=None
        return head
