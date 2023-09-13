from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = sum(nums[:k])
        max = cur
        for i in range(k, len(nums)):
            cur -= nums[i - k]
            cur += nums[i]
            if max < cur:
                max = cur
        return max / k