from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        res = []
        nums = sorted(nums)
        for first in range(0, len(nums)-2):
            second = first+1
            third = len(nums)-1
            while second < third:
                sum = nums[first] + nums[second] + nums[third]
                if sum == 0:
                    r = []
                    r.append(nums[first])
                    r.append(nums[second])
                    r.append(nums[third])
                    if r not in res:
                        res.append(r)
                    second += 1
                    third -= 1
                elif sum > 0:
                    third -= 1
                else:
                    second += 1
        return res

if __name__ == '__main__':
    solver = Solution()
    print(solver.threeSum([-1,0,1,2,-1,-4]))