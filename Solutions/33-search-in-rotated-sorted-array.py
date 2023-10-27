from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:

            k = (l + r) // 2
            if nums[k] == target:
                return k

            if nums[l] <= nums[k]:
                if target > nums[k] or target < nums[l]:
                    l = k + 1
                else:
                    r = k - 1
            else:
                if target < nums[k] or target > nums[r]:
                    r = k - 1
                else:
                    l = k + 1

        return -1

solution = Solution()
ret = solution.search([1,3], 3)