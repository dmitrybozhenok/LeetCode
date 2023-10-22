from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ret = []
        for i in range(len(nums) - 1):
            target = -nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                twosum = nums[j] + nums[k]
                if twosum == target:
                    if not ret.__contains__([nums[i], nums[j], nums[k]]):
                        ret.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif twosum < target:
                    j += 1
                else:
                    k -= 1

        return ret

solution = Solution()
ret = solution.threeSum([-1,0,1,2,-1,-4])


