from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] < nums[r]:
                break
            k = l + (r - l) // 2

            if nums[l] > nums[k]:
                r = k
            else:
                l = k + 1
        return nums[l]
