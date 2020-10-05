# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):

    def mergeTwoLists(self, l1, l2):
        # Solution1: normal
        dummy = ListNode(0)
        cur = dummy  # reference to dummy

        while l1 and l2:

            if l1.val < l2.val:
                # add the smaller one into new node list
                cur.next = ListNode(l1.val)
                # l1 move forward
                l1 = l1.next
            else:
                # add the smaller one into new node list
                cur.next = ListNode(l2.val)
                # l2 move forward
                l2 = l2.next
            # move the new node list forward=
            cur = cur.next

        if l1:
            cur.next = l1
        if l2:
            cur.next = l2

        return dummy.next


