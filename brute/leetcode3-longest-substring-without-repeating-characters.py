class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        length = len(s)
        count = [0 for x in range(0, length)]
        for i in range(0, length):
            l = 1
            check = [0 for x in range(0, 256)]
            check[ord(s[i])] = True
            count[i] = 1
            for j in range(i+1, length):
                if check[ord(s[j])] == True:
                    count[i] = l
                    break
                else:
                    check[ord(s[j])] = True
                    l += 1
                    count[i] = l
        for c in count:
            if c > res:
                res = c
        return res

if __name__ == '__main__':
    solver = Solution()
    assert solver.lengthOfLongestSubstring("abcabcbb") == 3
    assert solver.lengthOfLongestSubstring("bbbbb") == 1
    assert solver.lengthOfLongestSubstring("pwwkew") == 3

# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# Runtime: 2383 ms, faster than 5.01% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.4 MB, less than 14.13% of Python3 online submissions for Longest Substring Without Repeating Characters.