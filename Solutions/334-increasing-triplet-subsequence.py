from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = nums[0]
        maxvalue = max(nums)
        for i in range(1, len(nums) - 1):
            used = set()
            if used.__contains__(nums[i]):
                continue
            if nums[i] > first:
                if maxvalue > nums[i]:
                    return True
                used.add(nums[i])
            elif nums[i] < first:
                used.clear()
                first = nums[i]