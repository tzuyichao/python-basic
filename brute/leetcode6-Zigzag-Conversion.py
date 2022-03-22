class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n: int = len(s)
        unitSize: int = numRows + numRows - 2
        if n%unitSize == 0:
            width: int = (int)((numRows-1) * (n/unitSize))
        else:
            width: int = (int)((numRows-1) * (n/unitSize + 1))
        matrix = [["0"] * width for i in range(numRows)]
        count: int = 0
        for j in range(0, width):
            if count % unitSize >= 0 and count % unitSize < numRows:
                for i in range(0, numRows):
                    if count < n:
                        matrix[i][j] = s[count]
                        count+=1
            else:
                if count < n:
                    matrix[unitSize-count%unitSize][j] = s[count]
                    count+=1
        res: str = ""
        for i in range(0, numRows):
            for j in range(0, width):
                if matrix[i][j] != "0":
                    res += (matrix[i][j])
        return res

if __name__ == '__main__':
    solver = Solution()
    assert solver.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert solver.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"

# 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/ 
#
# Runtime: 2374 ms, faster than 5.00% of Python3 online submissions for Zigzag Conversion.
# Memory Usage: 24.5 MB, less than 5.04% of Python3 online submissions for Zigzag Conversion.