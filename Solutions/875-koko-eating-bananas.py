import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ret = r
        while l <= r:
            k = (l + r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / k)
            if hours <= h:
                ret = k
                r = k - 1
            else:
                l = k + 1
        return ret


solution = Solution()
ret = solution.minEatingSpeed([3,6,7,11], 8)

