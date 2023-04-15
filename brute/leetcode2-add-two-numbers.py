from re import L
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def len(self, l: Optional[ListNode]) -> int:
        if l is None:
            return 0
        else:
            c = l
            counter = 0
            while c is not None:
                c = c.next
                counter+=1
            return counter
    
    def carry(self, l: Optional[ListNode]) -> Optional[ListNode]:
        c = l
        isCarry = False
        c_val = 0
        while c is not None:
            if isCarry:
                c.val += c_val
            if c.val >= 10:
                isCarry = True
                c_val = int(c.val/10)
            else:
                isCarry = False
                c_val = 0
            c.val = c.val % 10
            if c.next is None and isCarry:
                c.next = ListNode(0)
            c = c.next
        return l

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        len1 = self.len(l1)
        len2 = self.len(l2)
        r1 = l1
        c1 = r1
        r2 = l2
        c2 = r2
        if len1 >= len2:
            while c1 is not None:
                if c2 is not None:
                    c1.val += c2.val
                    c2 = c2.next
                c1 = c1.next
            return self.carry(r1)
        else:
            while c2 is not None:
                if c1 is not None:
                    c2.val += c1.val
                    c1 = c1.next
                c2 = c2.next
            return self.carry(r2)

if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    solver = Solution()
    res = solver.addTwoNumbers(l1, l2)
    print(f"r: {res}")

# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/
# 
# Runtime: 64 ms, faster than 97.42% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14 MB, less than 57.69% of Python3 online submissions for Add Two Numbers.