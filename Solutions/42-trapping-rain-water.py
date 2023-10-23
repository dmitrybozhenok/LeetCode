from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        max_l = height[l]
        max_r = height[r]
        ret = 0
        while l < r:
            if max_l > max_r:
                r -= 1
                max_r = max(max_r, height[r])
                ret += max_r - height[r]
            else:
                l += 1
                max_l = max(max_l, height[l])
                ret += max_l - height[l]
        return ret


solution = Solution()
ret = solution.trap([4,2,3])
