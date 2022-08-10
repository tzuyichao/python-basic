class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        # print(nums)
        res = 0
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == nums[mid-1] or nums[mid] == nums[mid+1]:
                return nums[mid]
            elif nums[mid] < mid+1:
                right = mid
            else:
                left = mid
        return res