from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        window = []

        for i in range(k):
            while window and nums[i] > window[-1]:
                window.pop()
            window.append(nums[i])
        ret.append(window[0])

        for i in range(0, len(nums) - k):
            if nums[i] == window[0]:
                window.pop(0)
            while window and nums[i + k] > window[-1]:
                window.pop()
            window.append(nums[i + k])
            ret.append(window[0])

        return ret


solution = Solution()
ret = solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
