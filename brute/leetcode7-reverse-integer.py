import math

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        if x < 0:
            is_neg = True
        else:
            is_neg = False
        res = 0
        x = abs(x)
        l = math.floor(math.log10(x))
        while x/10 > 0:
            m = x % 10
            res += m * math.pow(10, l)
            l -= 1
            x = int(x / 10)
        res += int(x)
        if math.log2(res) > 31:
            return 0
        if is_neg:
            return -int(res)
        return int(res)

if __name__ == '__main__':
    solver = Solution()
    assert solver.reverse(123) == 321
    assert solver.reverse(0) == 0

# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/
#
# Runtime: 36 ms, faster than 82.19% of Python3 online submissions for Reverse Integer.
# Memory Usage: 13.9 MB, less than 70.16% of Python3 online submissions for Reverse Integer.