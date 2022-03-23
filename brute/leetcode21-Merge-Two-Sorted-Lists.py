from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def last(self, list: ListNode) -> ListNode:
        res = list
        while res.next != None:
            res = res.next
        return res

    def merge(self, list1: ListNode, list2: ListNode, res: ListNode):
        if list1 is None:
            self.last(res).next = list2
            return
        if list2 is None:
            self.last(res).next = list1
            return
        if list1.val >= list2.val:
            self.last(res).next = ListNode(list2.val)
            self.merge(list1, list2.next, res)
        else:
            self.last(res).next = ListNode(list1.val)
            self.merge(list1.next, list2, res)
        

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val > list2.val:
            res = ListNode(list2.val)
            self.merge(list1, list2.next, res)
        else:
            res = ListNode(list1.val)
            self.merge(list1.next, list2, res)
        return res
    
    def print(self, list: ListNode):
        c = list
        while c is not None:
            print(f"{c.val} ")
            c = c.next


if __name__ == '__main__':
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    solver = Solution()
    solver.print(solver.mergeTwoLists(l1, l2))


# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
#
# Runtime: 75 ms, faster than 11.43% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14.1 MB, less than 13.04% of Python3 online submissions for Merge Two Sorted Lists.