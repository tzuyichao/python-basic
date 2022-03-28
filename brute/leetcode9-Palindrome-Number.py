class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            s = str(x)
            l = len(s)
            r = l-1
            l = 0
            while l<r:
                if s[l] != s[r]:
                    return False
                r -= 1
                l += 1
            return True

# https://leetcode.com/problems/palindrome-number/
#
# Runtime: 75 ms, faster than 70.91% of Python3 online submissions for Palindrome Number.
# Memory Usage: 13.8 MB, less than 64.66% of Python3 online submissions for Palindrome Number.