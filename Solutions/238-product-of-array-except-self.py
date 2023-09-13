from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nlen = len(nums)
        ret = [1]*nlen
        post = 1
        for i in range(1, nlen):
            ret[i] = ret[i-1]*nums[i-1]
        for i in range(nlen - 2, -1, -1):
            post *= nums[i+1]
            ret[i] *= post
        return ret