from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = set(nums)
        longest = 1
        for n in nums:
            if n - 1 not in seen:
                length = 1
                j = n + 1
                while j in seen:
                    length += 1
                    j += 1
                longest = max(longest, length)
        return longest