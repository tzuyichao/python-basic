# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return None
        part1 = []
        part2 = []
        c = head
        while c is not None:
            if c.val >= x:
                part2.append(c)
            else:
                part1.append(c)
            c = c.next
        if len(part1) > 0:
            head = part1[0]
        else:
            return head
        c = head
        for i in range(1, len(part1)):
            c.next = part1[i]
            c = part1[i]
        for node in part2:
            c.next = node
            c = node
        c.next = None
        return head