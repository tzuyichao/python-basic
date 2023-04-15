class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        def find(numbsers, target, exclude):
            left = 0
            right = len(numbers)-1
            while left <= right:
                mid = left + (right-left)//2
                if mid != exclude and numbers[mid] == target:
                    return mid
                elif numbers[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        for idx, num in enumerate(numbers):
            other = find(numbers, target-num, idx)
            if other != -1:
                res = [idx+1, other+1]
        
        res.sort()
        return res