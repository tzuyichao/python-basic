from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height)-1
        while left < right:
            res = max(res, int(min(height[left], height[right]) * (right - left)))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return res
     

if __name__ == '__main__':
    solver = Solution()
    print(solver.maxArea([1,8,6,2,5,4,8,3,7]))

# https://leetcode.com/problems/container-with-most-water/
#
# Runtime: 875 ms, faster than 63.86% of Python3 online submissions for Container With Most Water.
# Memory Usage: 27.5 MB, less than 18.84% of Python3 online submissions for Container With Most Water.
#