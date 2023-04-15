class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength: int = 1
        low: int = 0
        high: int = 0
        start: int = 0
        l: int = len(s)
        for i in range(1, l):
            low = i-1
            high = i
            while low >=0 and high < l and s[low] == s[high]:
                if high-low+1 > maxLength:
                    start = low
                    maxLength = high-low+1
                low -= 1
                high += 1
            low = i-1
            high = i+1
            while low >= 0 and high < l and s[low] == s[high]:
                if high-low+1 > maxLength:
                    start = low
                    maxLength = high-low+1
                low -= 1
                high += 1
        return s[start:start+maxLength]
        
if __name__ == '__main__':
    solver = Solution()
    assert solver.longestPalindrome("babad") == "bab"
    assert solver.longestPalindrome("cbbd") == "bb"

# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
# 
# Runtime: 1363 ms, faster than 54.13% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 13.8 MB, less than 99.64% of Python3 online submissions for Longest Palindromic Substring.